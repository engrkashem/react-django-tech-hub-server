from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Job
from .serializers import JobSerializer
from users.models import User
from users.serializers import UserSerializer
# Create your views here.

class JobView(APIView):
    def get(self, request):
        jobs = Job.objects.all()
        serialized = JobSerializer(jobs, many=True)
        return Response(serialized.data, status= status.HTTP_200_OK)
    
    def post(self, request):
        job = request.data
        # user = User.objects.get(pk=job['creator'])
        # serializedUser = UserSerializer(user)
        # job['creator'] = serializedUser.data

        # print(job)
        serializer = JobSerializer(data = job)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    
    

class JobViewID(APIView):
    def get(self, request, pk):
        try:
            job = Job.objects.get(pk=pk)
        except:
            return Response(message = "Job not found", status= status.HTTP_404_NOT_FOUND)
        serialized = JobSerializer(job)
        return Response(serialized.data, status= status.HTTP_200_OK)