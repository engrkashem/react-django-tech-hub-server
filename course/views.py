from rest_framework.views import APIView
from .serializers import CourseSerializer, EnrollSerializer
from django.http import JsonResponse
from rest_framework import status
from django.http import Http404
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import Course, Enroll


class CourseView(APIView):
    # get course for list wish and individual
    def get(self, request, pk=None, format=None):
        if pk:
            try:
                course = Course.objects.get(pk=pk)
                serialized = CourseSerializer(course)
                return Response(serialized.data, status=status.HTTP_200_OK)
            except Course.DoesNotExist:
                raise Http404
        else:
            course = Course.objects.all().order_by('-create_at')
            serialized = CourseSerializer(course, many=True)
            return Response(serialized.data, status=status.HTTP_200_OK)
    # create new course

    def post(self, request, format=None):
        course = request.data
        serialized = CourseSerializer(data=course)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=status.HTTP_201_CREATED)
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)
    # find data by id

    def get_object(self, pk):
        return get_object_or_404(Course, pk=pk)
    # update course

    def put(self, request, pk, format=None):
        try:
            course = self.get_object(pk)
        except:
            return Response({"error": "Course not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = CourseSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            print(serializer.errors)  # Print the serializer errors
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # delete course

    def delete(self, request, pk, format=None):
        try:
            course = self.get_object(pk)
            course.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Course.DoesNotExist:
            return Response({"error": "Course not found"}, status=status.HTTP_404_NOT_FOUND)


class EnrollView(APIView):
    # get course for list wish and individual
    def get(self, request, pk=None, format=None):
        enroll = Enroll.objects.filter(student=pk).order_by('-enrolled_at')
        serialized = EnrollSerializer(enroll, many=True)
        return JsonResponse({'enroll': serialized.data}, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        enroll = request.data
        serialized = EnrollSerializer(data=enroll)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=status.HTTP_201_CREATED)
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)


class EnrollUserView(APIView):
    # get enrollments for specific user
    def get(self, request, user_id, format=None):
        try:
            enrollments = Enroll.objects.filter(student__id=user_id)
            serialized = EnrollSerializer(enrollments, many=True)
            return JsonResponse({'enrollments': serialized.data}, status=status.HTTP_200_OK)
        except Enroll.DoesNotExist:
            raise Http404
