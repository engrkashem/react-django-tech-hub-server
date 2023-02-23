from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Job
from .serializers import JobSerializer
# Create your views here.

class JobView(APIView):
    # Get all the jobs from the 
    def get(self, request):
        jobs = Job.objects.all()
        serialized = JobSerializer(jobs, many=True)
        return Response(serialized.data, status= status.HTTP_200_OK)

    # Post a new job
    def post(self, request):
        job = request.data
        serializer = JobSerializer(data = job)
        
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Job posted successfully'}, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    
    

class JobViewID(APIView):
    # Get a Job with primary key
    def get(self, request, pk):
        try:
            job = Job.objects.get(pk=pk)
        except:
            return Response({'message':'Job not found'}, status= status.HTTP_404_NOT_FOUND)
        serialized = JobSerializer(job)
        return Response(serialized.data, status= status.HTTP_200_OK)
    
    # Update a Job with primary key
    def put(self, request, pk):
        job = request.data
        try:
            job_from_db = Job.objects.get(pk=pk)
        except:
            return Response({'message' : 'Job not found'}, status= status.HTTP_404_NOT_FOUND)

        serialized = JobSerializer(job_from_db, data = job)

        if serialized.is_valid():
            serialized.save()
            return Response({'message': 'Job updated successfully'}, status= status.HTTP_200_OK)
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # Delete a Job with primary key
    def delete(self, request, pk):
        job = request.data

        try:
            job_from_db = Job.objects.get(pk=pk)
        except:
            return Response({'message' : 'Job not found'}, status=status.HTTP_404_NOT_FOUND)
        
        job_from_db.delete()
        return Response({'message' : 'Job deleted successfully'}, status=status.HTTP_200_OK)
        

        
        