from django.forms import ValidationError
from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView, View
from rest_framework.response import Response
from rest_framework import permissions
from .serializers import UserSerializer
from profiles.models import UserProfile
# Create your views here.

class UserViewSet(ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer
    def get_queryset(self):
        contains = self.kwargs.get('contains')
        queryset = UserProfile.objects.filter(username__contains=contains)
        return queryset
    

