from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    
    for people in peoples:
        print(people['name'])
    
    peoples=[{'name':'John','age':23},{'name':'Doe','age':24},{'name':'Jane','age':25},{'name':'Danisson','age':26}]
    return render(request,'index.html',context={'peoples':peoples})

    


def about(request):
    return HttpResponse("About Us")