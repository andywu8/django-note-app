from django.urls import path 
from django.urls import path, include
from . import views 

app_name = 'social'
urlpatterns = [
    path('', views.UserList.as_view(), name='home'),
]