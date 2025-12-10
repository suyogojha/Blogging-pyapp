
from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.urls import include    
from blogs import views as BlogsView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name='home'),
    path('category/', include('blogs.urls')),
    path('blogs/<slug:slug>/', BlogsView.blogs, name='blogs'),
    # search endpoint for blogs
    path('blogs/search', BlogsView.search, name='search'),
    # register url 
    path('register/', views.register, name='register'),
    # login url 
    path('login/', views.login, name='login'),
    # logout url 
    path('logout/', views.logout, name='logout'),
    
    
    # dashboard urls 
    path('dashboard/', include('dashboards.urls')),
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
