from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Job, Applications
from .serializers import JobSerializer, ApplicationSerializer
from users.models import User
# Create your views here.

class JobView(APIView):
    # Get all the jobs from the 
    def get(self, request):
        param = request.query_params

        # try:
        #     filtered_jobs = Job.objects.filter(creator = User.objects.get(email = param['email']).id)
        # except:
        #     filtered_jobs = Job.objects.none()

        if param['search'] or param['email']:
            # if param['email']:
            #     userId = 
            #     # print(userId, "hi")
            #     filtered_jobs = Job.objects.filter(creator = userId)
            #     serializer = JobSerializer(filtered_jobs, many = True)
            #     return Response(serializer.data)

            if param['email'] and param['search']:
                try:
                    jobs_from_db = Job.objects.filter(skill_requirements__icontains = param['search'])
                    # filtered_jobs = jobs_from_db.filter(creator = User.objects.get(email = param['email']).id)
                    # try:
                    jobs_from_db = jobs_from_db.filter(creator = User.objects.get(email = param['email']).id)
                except Exception as exp:
                    jobs_from_db = Job.objects.none()
            elif param['search']:
                jobs_from_db = Job.objects.filter(skill_requirements__icontains = param['search'])
            
            else:
                try:
                    jobs_from_db = Job.objects.filter(creator = User.objects.get(email = param['email']).id)
                except Exception as exp:
                    jobs_from_db = Job.objects.none()

            # jobs = jobs_from_db | filtered_jobs
            # print(jobs)
            serialized = JobSerializer(jobs_from_db, many = True)
            return Response({'jobs':serialized.data}, status=status.HTTP_200_OK)
        else:
            jobs = Job.objects.all()
            serialized = JobSerializer(jobs, many=True)
            return Response({'jobs':serialized.data}, status= status.HTTP_200_OK)

    

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
        

class ApplicationView(APIView):
    def post(self, request):
        application = request.data
        serializer = ApplicationSerializer(data=application)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"Applied Successfully"}, status=status.HTTP_200_OK)
        return Response({"message": serializer.errors} , status=status.HTTP_200_OK)
    
    def get(self, request, pk):
        try:
            applications = Applications.objects.filter(job=pk)
        except:
            return Response({"message": "No application found"}, status=status.HTTP_200_OK)
        
        serializer = ApplicationSerializer(applications, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)