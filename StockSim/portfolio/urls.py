from django.urls import path
from . import views

app_name = 'portfolio'
urlpatterns = [
    path(r'', views.IndexView.as_view(), name='home'),
]