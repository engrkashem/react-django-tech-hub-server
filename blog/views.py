from rest_framework.views import APIView
from .models import BlogModel
from .serializers import BlogSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class BlogView(APIView):
    def get(self, request):
        blogs_obj=BlogModel.objects.all()
        serialized_blog=BlogSerializer(blogs_obj, many=True)
        return Response(serialized_blog.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        blog_obj=request.data
        serialized_blog=BlogSerializer(data=blog_obj)
        if serialized_blog.is_valid():
            serialized_blog.save()
            return Response(serialized_blog.data, status=status.HTTP_201_CREATED)
        return Response(serialized_blog.errors, status=status.HTTP_400_BAD_REQUEST)