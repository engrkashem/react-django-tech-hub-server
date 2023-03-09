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
        # for u in user:
        #     print(u.userName, u.email, u.skill_set)
        
        # serialize them 
        serialized = UserSerializer(user, many = True)
        # print(serialized)
        # return json
        
        # return JsonResponse({'users':serialized.data}, status=status.HTTP_200_OK)
        return Response(serialized.data, status=status.HTTP_200_OK)
    
    def post(self, request, format=None):
        user = request.data
        # print(user)
        # print(type(user))
        already_exist=User.objects.filter(email=user['email']).exists()
        # print(already_exist, type(already_exist))
        if already_exist:
            return Response({'message':'User Already Exist'} , status=status.HTTP_406_NOT_ACCEPTABLE)
        
        serialized=UserSerializer(data=user)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=status.HTTP_201_CREATED)
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request):
        updated_user=request.data
        try:
            get_user_from_db=User.objects.get(email=updated_user['email'])
        except:
            return Response({'message':'User not found'}, status=status.HTTP_404_NOT_FOUND)

        serialized=UserSerializer(get_user_from_db, data=updated_user)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=status.HTTP_200_OK)
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request):
        user = request.data
        try:
            get_user = User.objects.get(email = user['email'])
        except:
            return Response({'message':'User not found'}, status=status.HTTP_404_NOT_FOUND)
        get_user.delete()
        return Response({'message': 'User deleted successfully'}, status = status.HTTP_204_NO_CONTENT)
