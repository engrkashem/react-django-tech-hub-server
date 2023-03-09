from rest_framework import serializers
from .models import Job, Applications
from users.serializers import UserSerializer
from users.models import User

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'

    def to_representation(self, obj):
        self.fields['creator'] = UserSerializer(read_only=True)
        return super().to_representation(obj)

    
class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applications
        fields = '__all__'

    def to_representation(self, instance):
        self.fields['creator'] = UserSerializer(read_only=True)
        return super().to_representation(instance)