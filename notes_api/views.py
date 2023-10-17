from django.shortcuts import render
# from rest_framework import generics
from django.views import generic
from .models import Note
from .serializers import NoteSerializer
from django.shortcuts import get_object_or_404, render
from .forms import NoteForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required


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

    # this function will return the notes list 
# @permission_classes([IsAuthenticated])
class NoteDetail(generic.DetailView):
    queryset = Note.objects.all()
    context_object_name = 'note_detail'
    template_name = "notes_api/detail.html"

class EditNote(generic.DetailView):
    queryset = Note.objects.all()
    context_object_name = 'note_detail'
    template_name = "notes_api/edit.html"

def update_note(request, pk):
    print("request", request)
    if request.method=="POST":
        note = NoteForm(request.POST)
        if note.is_valid():
            note.save()
            return HttpResponseRedirect(reverse('notes_api:home'))

def add_note(request):
    if request.method=="POST":
        note = NoteForm(request.POST)
        print("note", note)
        if note.is_valid():
            note.user = request.user
            # print("request.user", request.user)
            note.save()
            request.user.note.add(note)
            return HttpResponseRedirect(reverse('notes_api:home'))

def delete_note(request, pk):
    note = get_object_or_404(Note, pk=pk)
    note.delete()
    return HttpResponseRedirect(reverse('notes_api:home'))

