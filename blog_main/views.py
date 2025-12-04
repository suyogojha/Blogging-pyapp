
from django.shortcuts import render

from blogs.models import *


def home(request):
    categories = Category.objects.all()
    featured_posts = Blog.objects.filter(is_featured=True)
    context = {
        'categories': categories,
        'featured_posts': featured_posts,
    }
    return render(request, 'home.html', context)


# 1:15:26