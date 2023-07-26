from django.http import HttpResponse
from rest_framework.generics import ListAPIView, UpdateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from .serializers import UserSerializer, FollowingSerializer
from profiles.models import UserProfile
# Create your views here.

class UserViewSet(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, username):
        try:
            queryset = UserProfile.objects.get(username=username)
            serializer = UserSerializer(queryset)
            return Response(serializer.data)
        except:
            return Response("No existe ningun usuario")

class UserContainsViewSet(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, contains):
        queryset = UserProfile.objects.filter(username__contains=contains)
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

class FollowingViewSet(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, username):
        if username == request.user.username:
            queryset = UserProfile.objects.get(username=self.request.user.username)
            serializer = FollowingSerializer(queryset)
            return Response(serializer.data)
        return Response("No existe el usuario")
    
    def put(self, request, username, format=None):
        if username == request.user.username:
            queryset = UserProfile.objects.get(username=request.user.username)
            serializer = FollowingSerializer(queryset, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)

