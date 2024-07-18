from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def profile(request):
    return render(request, 'profile.html')

def testimonials(request):
    return render(request, 'testimonials.html')

def news(request):
    return render(request, 'news.html')

def contactus(request):
    return render(request, 'contactus.html')
