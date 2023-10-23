from django.shortcuts import render
from django.views import generic
from django.contrib.auth.models import User


# Create your views here.
class UserList(generic.ListView):
    template_name = "social/index.html"
    context_object_name = 'all_users'
    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        all_users = User.objects.all()
        print("all_users", all_users)
        return all_users
        # this gets all notes
        # return Note.objects.all().order_by('-updated')
        # return None