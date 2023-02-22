from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Job
from .serializers import JobSerializer
# Create your views here.

class JobView(APIView):
    def get(self, request):
        try:
            pk = request.query_params['id']
            job = Job.objects.get(pk=pk)
            serialized = JobSerializer(job)
            return Response(serialized.data, status= status.HTTP_200_OK)
        except:
            jobs = Job.objects.all()
            serialized = JobSerializer(jobs, many=True)
            return Response(serialized.data, status= status.HTTP_200_OK)
    
    # def get(self, request, pk, format=None):
    #     pass
