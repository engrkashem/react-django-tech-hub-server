from rest_framework import serializers
from .models import Job
from users.serializers import UserSerializer
from users.models import User

class JobSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Job
        fields = ['title', 'content', 'created_at', 'updated_at', 'photo_url','user']

    def get_user(self, obj):
        user_data = User.objects.get(id=obj.creator.id)
        return {'id': user_data.id ,'userName': user_data.userName, 'photo_url': user_data.photo_url, 'profession': user_data.profession}

    