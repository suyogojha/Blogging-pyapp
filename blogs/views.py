from django.shortcuts import get_object_or_404, render
from . models import *



def posts_by_category(request, category_id):
    #fetch posts based on category_id   
    posts = Blog.objects.filter(category=category_id, status="Published")
    
    try:
    # fetch category name #use this when we want to do some custom action if category not found
        category = Category.objects.get(pk=category_id) 
    except:
        return render(request, '404.html')

    # fetch category name #use get_object_or_404 to handle not found case and show 404 page
    # category = get_object_or_404(Category, pk=category_id)

    context = {
        'posts': posts, 
        'category': category, 
    }
    return render(request, 'posts_by_category.html', context)    