from rest_framework import serializers
from .models import Note 

# Serializer for the Note model
# Convert the Note model into JSON
class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note 
        fields = '__all__'