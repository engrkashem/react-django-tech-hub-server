from rest_framework import serializers
from .models import MessageModel
from users.serializers import UserSerializer


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model=MessageModel
        fields='__all__'

    def to_representation(self, instance):
        self.fields['sender']=UserSerializer(read_only=True)
        return super().to_representation(instance)