'''Documentation String'''
from rest_framework import serializers
from .models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    '''Documentation String'''
    class Meta:
        '''Documentation String'''
        model = UserProfile
        fields = "__all__"
