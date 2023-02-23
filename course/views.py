from rest_framework.views import APIView
from .serializers import CourseSerializer
from django.http import JsonResponse
from rest_framework import status
from django.http import Http404
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import Course
class CourseView(APIView):
    #get course for list wish and individual 
    def get(self, request, pk=None, format=None):
        if pk:
            try:
                course = Course.objects.get(pk=pk)
                serialized = CourseSerializer(course)
                return JsonResponse({'course': serialized.data}, status=status.HTTP_200_OK)
            except Course.DoesNotExist:
                raise Http404
        else:
            course = Course.objects.all()
            serialized = CourseSerializer(course, many=True)
            return JsonResponse({'course': serialized.data}, status=status.HTTP_200_OK)
    #create new course
    def post(self, request, format=None):
        course = request.data
        serialized = CourseSerializer(data=course)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=status.HTTP_201_CREATED)
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)
    #find data by id
    def get_object(self, pk):
        return get_object_or_404(Course, pk=pk)
    #update course
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
    #delete course
    def delete(self, request, pk, format=None):
        try:
            course = self.get_object(pk)
            course.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Course.DoesNotExist:
            return Response({"error": "Course not found"}, status=status.HTTP_404_NOT_FOUND)

