from django.urls import path 

from . import views 
app_name = 'notes_api'
urlpatterns = [
    path('notes/', views.NoteList.as_view(), name='note-list'),
    path('notes/<str:pk>/', views.NoteDetail.as_view(), name='note-detail'),
]