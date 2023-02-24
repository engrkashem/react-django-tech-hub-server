from rest_framework import serializers
from .models import Course
from users.serializers import UserSerializer

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"

    def to_representation(self, instance):
        self.fields['instructor'] = UserSerializer(read_only=True)
        return super().to_representation(instance)
