
from django.shortcuts import render

from blogs.models import *
from assignments.models import *

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


