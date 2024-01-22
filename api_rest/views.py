from django.http import HttpResponse
from rest_framework.generics import ListAPIView, UpdateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from .serializers import UserSerializer, FollowingSerializer, PublicationSerializer
from profiles.models import UserProfile, Publication
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

class PublicationViewSet(APIView):
    def get(self,request, id):
        queryset = Publication.objects.get(id=id)
        serializer = PublicationSerializer(queryset)
        return Response(serializer.data)
    
    def put(self, request, id):
        queryset = Publication.objects.get(id=id)
        if queryset.likes == '' or queryset.likes == None:
            likes = [str(request.user.id)]
        else:
            if str(request.user.id) in queryset.likes.split(","):
                likes = queryset.likes.split(",")
                likes.remove(str(request.user.id))
                if len(likes) == 0:
                    likes = ''
            else:
                likes = queryset.likes.split(",")
                likes.append(request.data["likes"])
    
        serializer = PublicationSerializer(queryset, data={'likes':','.join(likes)})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

