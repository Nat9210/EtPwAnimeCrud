"""
URL configuration for djangocrud project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from taskcrud import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name = 'home'),
    path('signup/', views.signup, name = 'signup'),
    path('crud/', views.crud, name = 'crud'),
    path('crud/create/', views.create_crud, name = 'create_crud'),
    path('crud/<int:media_id>/', views.detail_crud, name = 'detail_crud'),
    path('crud/<int:media_id>/delete', views.delete_crud, name = 'delete_crud'),
    path('logout/', views.signout, name = 'logout'),
    path('signin/', views.signin, name = 'signin'),
    path('news/', views.news_view, name='news'),
    path('perfil/', views.perfil_view, name='perfil'),
    
    
]
