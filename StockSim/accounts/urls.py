from django.urls import path

from . import views

app_name = 'accounts'
urlpatterns=[
    path('login/', views.loginUser, name='loginUser'),
    path('register/', views.register, name='register'),
    path('logout/', views.logoutUser, name='logoutUser'),
    path('profile/', views.userProfile, name='userProfile'),
    path('', views.HomeView.as_view(), name='home'),
]