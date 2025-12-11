from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from . models import *
from django.db.models import Q


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


def blogs(request, slug):
    single_blog = get_object_or_404(Blog, slug=slug, status='Published')
    if request.method == 'POST':
        comment = Comment()
        comment.user = request.user
        comment.blog = single_blog
        comment.comment = request.POST['comment']
        comment.save()
        return HttpResponseRedirect(request.path_info)

    # Comments
    comments = Comment.objects.filter(blog=single_blog)
    comment_count = comments.count()
    
    context = {
        'single_blog': single_blog,
        'comments': comments,
        'comment_count': comment_count,
    }
    return render(request, 'blogs.html', context)



def search(request):
    keyword = request.GET.get('keyword')
    blogs = Blog.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword) | Q(blog_body__icontains=keyword), status="Published")
    context ={
        'blogs': blogs,
        'keyword': keyword,
    }
    return render(request, 'search.html', context)