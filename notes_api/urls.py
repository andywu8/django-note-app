from django.urls import path 

from . import views 
app_name = 'notes_api'
urlpatterns = [
    path('', views.NoteList.as_view(), name='note_list'),
    path('<int:pk>/', views.NoteDetail.as_view(), name='note_detail'),
    path('add_note/', views.add_note, name='add_note'),
]