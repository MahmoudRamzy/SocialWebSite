from django.urls import path, include
from . import views

urlpatterns = [
    # post views
    path('', include('django.contrib.auth.urls')),
    path('', views.dashboard, name='dashboard'),  # change password urls
    path('register/', views.register, name='register'),
    path('edit/', views.edit, name='edit'),
    path('users/follow/', views.user_follow, name='user_follow'),
    path('users/', views.user_list, name='user_list'),
    path('users/<username>/', views.user_detail, name='user_detail'),
]
