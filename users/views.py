from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer
from django.http import JsonResponse
from rest_framework import status
from .models import User

class UserView(APIView):
    def get(self, request, format=None):
        # get all the users
        user = User.objects.all()
        # serialize them 
        serialized = UserSerializer(user, many = True)
        # return json
        
        return JsonResponse({'users':serialized.data}, status=status.HTTP_200_OK)
        # return Response(serialized.data, status=status.HTTP_200_OK)
    
    def post(self, request, format=None):
        pass