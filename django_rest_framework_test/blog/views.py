from django.shortcuts import render
import django_filters
from rest_framework import viewsets, filters
from django.contrib.auth.models import User

from .models import Entry
from .serializer import UserSerializer, EntrySerializer

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class EntryViewSet(viewsets.ModelViewSet):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
    filter_fields = ('author', 'status')