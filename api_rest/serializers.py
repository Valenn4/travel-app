from rest_framework import serializers
from profiles.models import UserProfile, Publication

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id','username']

class FollowingSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['following']

class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = ['id', 'likes']
