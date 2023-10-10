from django.shortcuts import render
# from rest_framework import generics
from django.views import generic
from .models import Note
from .serializers import NoteSerializer
from django.shortcuts import get_object_or_404, render
from .forms import NoteForm
from django.http import HttpResponseRedirect
from django.urls import reverse

# @permission_classes([IsAuthenticated])
class NoteList(generic.ListView):
    template_name = "notes_api/index.html"
    context_object_name = "latest_notes_list"

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Note.objects.all().order_by('-updated')

# class NoteList(generics.ListCreateAPIView):
#     # context_object_name = "latest_notes_list"
#     # template_name = "notes_api/index.html"
#     # def get_queryset(self):
#     queryset = Note.objects.all().order_by('-updated')
#     serializer_class = NoteSerializer
#     # return serializer_class



    # this function will return the notes list 
 
# @permission_classes([IsAuthenticated])
class NoteDetail(generic.DetailView):
    queryset = Note.objects.all()
    context_object_name = 'note_detail'
    # serializer_class = NoteSerializer
    template_name = "notes_api/detail.html"
# class NoteDetail(generic.RetrieveUpdateDestroyAPIView):
#     queryset = Note.objects.all()
#     serializer_class = NoteSerializer


def add_note(request):
    if request.method=="POST":
        note = NoteForm(request.POST)
        # note = NoteForm(request.POST)
        if note.is_valid():
            note.save()
            return HttpResponseRedirect(reverse('notes_api:note_list'))
