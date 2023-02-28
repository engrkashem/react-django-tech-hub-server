from rest_framework import serializers
from .models import Course, Enroll
from users.serializers import UserSerializer

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"

    def to_representation(self, instance):
        self.fields['instructor'] = UserSerializer(read_only=True)
        return super().to_representation(instance)


class EnrollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enroll
        fields = "__all__"

    def to_representation(self, instance):
        self.fields['Enroll_User'] = UserSerializer(read_only=True)
        self.fields['Enroll_Course'] = CourseSerializer(read_only=True)
        return super().to_representation(instance)
