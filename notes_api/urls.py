from django.urls import path 

from . import views 
app_name = 'notes_api'
urlpatterns = [
    path('', views.NoteList.as_view(), name='note_list'),
    path('detail/<int:pk>/', views.NoteDetail.as_view(), name='note_detail'),
    path('add_note/', views.add_note, name='add_note'),
    path('edit/<int:pk>/', views.EditNote.as_view(), name='edit_note'),
    path('edit/<int:pk>/update_note', views.update_note, name='update_note'),
]