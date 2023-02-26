from rest_framework.views import APIView
from .models import BlogModel
from .serializers import BlogSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class BlogViewID(APIView):
    # get a blog by id
    def get(self,request,pk):
        try:
            blog_obj=BlogModel.objects.get(id=pk)
        except:
            return Response({'message':'Blog not found in the database'}, status=status.HTTP_400_BAD_REQUEST)
        
        serialized_blog=BlogSerializer(blog_obj)
        return Response(serialized_blog.data, status=status.HTTP_200_OK)
    

    # Update a blog
    def patch(self,request, pk):
        try:
            blog_by_id_from_db=BlogModel.objects.get(id=pk)
        except:
            return Response( status=status.HTTP_400_BAD_REQUEST)
        
        updated_blog=request.data
        serialized=BlogSerializer(blog_by_id_from_db, data=updated_blog)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=status.HTTP_200_OK)
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # delete a blog
    def delete(self,request, pk):
        try:
            blog_by_id_from_db=BlogModel.objects.get(id=pk)
        except:
            return Response( status=status.HTTP_400_BAD_REQUEST)
        blog_by_id_from_db.delete()
        return Response({'message':'Blog is deleted'},status=status.HTTP_204_NO_CONTENT)



class BlogView(APIView):
    # get all blog in the database
    def get(self, request):
        blogs_obj=BlogModel.objects.all()
        serialized_blog=BlogSerializer(blogs_obj, many=True)
        return Response(serialized_blog.data, status=status.HTTP_200_OK)

    
    # create/post a blog to database
    def post(self, request):
        blog_obj=request.data
        if not blog_obj.get('blog_heading'):
            return Response( status=status.HTTP_400_BAD_REQUEST)
        # print(blog_obj)
        serialized_blog=BlogSerializer(data=blog_obj)
        if serialized_blog.is_valid():
            serialized_blog.save()
            return Response(serialized_blog.data, status=status.HTTP_201_CREATED)
        return Response(serialized_blog.errors, status=status.HTTP_400_BAD_REQUEST)
    
    