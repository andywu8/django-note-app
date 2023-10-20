from django.shortcuts import render
from django.views import generic

# Create your views here.
class UserList(generic.ListView):
    template_name = "social/index.html"
    context_object_name = 'users'
    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        # this gets all notes
        # return Note.objects.all().order_by('-updated')
        return None