from django.shortcuts import render

# Create your views here.
# api_app/views.py

from rest_framework import viewsets
from .models import Message
from .serializers import MessageSerializer

class MessageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows messages to be viewed or edited.
    """
    queryset = Message.objects.all().order_by('-created_at')
    serializer_class = MessageSerializer