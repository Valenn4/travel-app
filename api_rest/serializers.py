from rest_framework import serializers
from profiles.models import UserProfile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id','username']

class FollowingSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['following']