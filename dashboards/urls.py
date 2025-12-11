from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),   
    path('categories/', views.categories, name='categories'),  
    
    # add categories 
    path('categories/add/', views.add_category, name='add_category'), 

    # edit categories 
    path('categories/edit/<int:pk>/', views.edit_category, name='edit_category'), 

    # delete categories 
    path('categories/delete/<int:pk>/', views.delete_category, name='delete_category'), 
    
    #blog posts crud urls can be added here
    
    path('posts/', views.posts, name='posts'),  
    
    # add post
    path('posts/add/', views.add_post, name='add_post'),  
     
    # edit post
    path('posts/edit/<int:pk>/', views.edit_post, name='edit_post'),  
     
    # delete post
    path('posts/delete/<int:pk>/', views.delete_post, name='delete_post'),  
 
 
    # users
    path('users/', views.users, name='users'),    
 
    # adding users
    path('users/add/', views.add_user, name='add_user'),    

    # edit user
    path('users/edit/<int:pk>/', views.edit_user, name='edit_user'),  

    # delete user
    path('users/delete/<int:pk>/', views.delete_user, name='delete_user'),  
]