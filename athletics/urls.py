from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('testimonials/', views.testimonials, name='testimonials'),
    path('news/', views.news, name='news'),
    path('contactus/', views.contactus, name='contactus'),
]
