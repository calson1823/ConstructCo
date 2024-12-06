from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('blog-details/', views.blog_details, name='blog-details'),
    path('contact/', views.contact, name='contact'),
    path('project-details/', views.project_details, name='project-details'),
    path('projects/', views.projects, name='projects'),
    path('service-details/', views.service_details, name='service-details'),
    path('services/', views.services, name='services'),
    path('starter-page/', views.starter_page, name='starter-page'),
    path('', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('quote/', views.quote, name='quote'),
    path('showcontact/', views.showcontact, name='showcontact'),
    path('showcomment/', views.showcomment, name='showcomment'),
    path('upload-blog/', views.upload_blog, name='upload-blog'),
]
