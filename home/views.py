from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import User, Startup, PitchRequest
from rest_framework.generics import ListAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
from django.http import JsonResponse
from django.contrib.auth import authenticate


# Login Page
@api_view(['post'])
def login_page(request):
        data = json.loads(request.body)
        username = data.get('eurekaid')  # Replace with 'eurekaid' if needed
        password = data.get('password')

        user = authenticate(username=username, password=password)
        print(username, password)
        if user:
            return JsonResponse({
                'message': 'Login successful!',
                'status': 'success',
                'role': user.role  # Pass the role to the frontend
            }, status=200)
        return JsonResponse({'message': 'Invalid credentials.', 'status': 'error'}, status=401)

        return JsonResponse({'message': 'Invalid request method.'}, status=405)

def dashboard(request):
    user = request.user
    
    if user.role == 'admin':
        print(user.role)
        return render(request,'admin_dashboard.html')
    elif user.role == 'coordinator':
        print(user.role)
        return render(request,'coordinator_dashboard.html')
    elif user.role == 'jury':
        print(user.role)
        return render (request,'jury_dashboard.html')
    else:
        return render(request, 'error.html', {'message': 'Invalid role'})

# Admin Dashboard
@login_required
def admin_dashboard(request):
    if request.user.role != 'admin':
        return redirect('login_page')
    startups = Startup.objects.all()
    return render(request, 'admin_dashboard.html', {'startups': startups})

# Approve/Reject Requests
@login_required
def admin_approve_request(request, pk):
    if request.user.role != 'admin':
        return redirect('login_page')
    pitch_request = get_object_or_404(PitchRequest, pk=pk)
    if pitch_request.startup.pitching_room_empty:
        pitch_request.approved = True
        pitch_request.startup.status = 'approved'
        pitch_request.startup.pitching_room_empty = False
    else:
        pitch_request.approved = False
    pitch_request.save()
    pitch_request.startup.save()
    return redirect('admin_dashboard')

# Coordinator Dashboard
@login_required
def coordinator_dashboard(request):
    if request.user.role != 'coordinator':
        return redirect('login_page')
    startups = Startup.objects.all()
    return render(request, 'coordinator_dashboard.html', {'startups': startups})

# Add Startup
@login_required
def add_startup(request):
    if request.user.role != 'coordinator':
        return redirect('login_page')
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        slides = request.FILES.get('slides')
        Startup.objects.create(name=name, description=description, slides=slides)
        return redirect('coordinator_dashboard')
    return render(request, 'add_startup.html')

@login_required
def startup_list(request):
    if not request.user.is_coordinator:
        return render(request, 'unauthorized.html')

    startups = Startup.objects.all()
    return render(request, 'startup_list.html', {'startups': startups})



# Jury Dashboard
@login_required
def jury_dashboard(request):
    if request.user.role != 'jury':
        return redirect('login_page')
    startups = Startup.objects.filter(status='approved')
    return render(request, 'jury_dashboard.html', {'startups': startups})

@api_view(['GET'])
def startup_list_api(request):
    # CODE GOES HERE
    authheader=request.headers['Authorization']
    print(authheader)
    req_user=User.objects.get(username=authheader)
    if req_user.role == 'jury':
        # return render(request, 'unauthorized.html')
        return Response({'error': 'Unauthorized'}, status=403)

    startups = Startup.objects.all()
    data = list(startups.values())

    # return render(request, 'startup_list.html', {'startups': startups})
    return Response(data)
