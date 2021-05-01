from rest_framework import serializers
from .models import opinion
from django.contrib.auth.models import User

class UserSerilizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields='__all__'
    
class OpinionSerilizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = opinion
        fields='__all__'
    
