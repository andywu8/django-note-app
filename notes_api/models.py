from django.db import models

# model for the notes
class Note(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # return string representation of the object
    def __str__(self):
        return self.title
    

