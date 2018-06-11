from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Entry

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')

class EntrySerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Entry
        fields = ('title', 'body', 'created_at', 'status', 'author')