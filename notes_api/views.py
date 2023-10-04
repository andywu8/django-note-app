from django.shortcuts import render
from rest_framework import generics
from .models import Note
from .serializers import NoteSerializer

# @permission_classes([IsAuthenticated])
class NoteList(generics.ListCreateAPIView):
    queryset = Note.objects.all().order_by('-updated')
    serializer_class = NoteSerializer

# @permission_classes([IsAuthenticated])
class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
