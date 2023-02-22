from rest_framework import serializers
from .models import Job
from users.serializers import UserSerializer

class JobSerializer(serializers.ModelSerializer):
    creator = UserSerializer(read_only=True)
    class Meta:
        model = Job
        fields = '__all__'