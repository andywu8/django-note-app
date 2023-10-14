from django.urls import path 
from django.contrib.auth.views import LogoutView
from django.urls import path, include

from . import views 
app_name = 'notes_api'
urlpatterns = [
    path('', views.NoteList.as_view(), name='note_list'),
    path('accounts/', include('allauth.urls')),
    path('logout', LogoutView.as_view(), name='logout'),
    path('detail/<int:pk>/', views.NoteDetail.as_view(), name='note_detail'),
    path('add_note/', views.add_note, name='add_note'),
    path('delete_note/<int:pk>/', views.delete_note, name='delete_note'),
    path('edit/<int:pk>/', views.EditNote.as_view(), name='edit_note'),
    path('edit/<int:pk>/update_note', views.update_note, name='update_note'),
]