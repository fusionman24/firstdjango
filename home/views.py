from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import User, Startup, PitchRequest

# Login Page
def login_page(request):
    return render(request, 'login.html')

def dashboard(request):
    return render(request, 'dashboard.html', {'user': request.user})


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

# Jury Dashboard
@login_required
def jury_dashboard(request):
    if request.user.role != 'jury':
        return redirect('login_page')
    startups = Startup.objects.filter(status='approved')
    return render(request, 'jury_dashboard.html', {'startups': startups})