from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context_dict = {}

    return render(request, 'ptfinderApp/index.html', context=context_dict)

def contactus(request):
    context_dict = {}
    
    return render(request, 'ptfinderApp/contact-us.html', context=context_dict)
    
def book(request):
    context_dict = {}
    
    return render(request, 'ptfinderApp/book.html', context=context_dict)
    