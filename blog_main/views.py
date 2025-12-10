
from django.shortcuts import render, redirect

from blogs.models import *
from assignments.models import *
from blog_main.forms import *
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib import auth
def home(request):
    featured_posts = Blog.objects.filter(is_featured=True, status="Published").order_by('created_at')
    posts = Blog.objects.filter(is_featured=False, status="Published")
    
    
    # fetch about us section data
    try:
        about = About.objects.get()
    except:
        about = None
    
    context = {
        'featured_posts': featured_posts,
        'posts': posts,
        'about': about,
    }
    return render(request, 'home.html', context)


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RegisterForm()
    context = {
        'form': form,
    }
    return render(request, 'register.html', context)



def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid(): 
            # log the user in
            username = form.cleaned_data['username'] #username inside brackets must also be same as in the AuthenticationForm
            password = form.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
            return redirect('dashboard')
    form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'login.html', context)


def logout(request):
    auth.logout(request)
    return redirect('home')