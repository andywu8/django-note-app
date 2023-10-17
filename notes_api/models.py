from django.db import models
from django.contrib.auth.models import User

# model for the notes
class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="note", null=True) # <--- added
    title = models.CharField(max_length=100, null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # return string representation of the object
    def __str__(self):
        return self.title
    

class Item(models.Model):
    note = models.ForeignKey(Note, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    complete = models.BooleanField()

    def __str__(self):
	    return self.text

