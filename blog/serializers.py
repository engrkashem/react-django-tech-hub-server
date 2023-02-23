from rest_framework import serializers
from .models import BlogModel
from users.serializers import UserSerializer

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model=BlogModel
        fields='__all__'

    def to_representation(self, instance):
        self.fields['blog_creator']=UserSerializer(read_only=True)
        return super().to_representation(instance)