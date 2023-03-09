from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import MessageModel
from .serializers import MessageSerializer

# Create your views here.
class MessageView(APIView):
    def get(self, request):
        all_message_obj=MessageModel.objects.all()
        serialized_message=MessageSerializer(all_message_obj, many=True)
        return Response(serialized_message.data, status=status.HTTP_200_OK)
    
    def post(self,request):
        message_obj=request.data

        if not message_obj.get('sender'):
            return Response({'message': 'sender is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        if not message_obj.get('message_body'):
            return Response({'message': 'Message Body is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        serializedMessage=MessageSerializer(data=message_obj)
        if serializedMessage.is_valid():
            serializedMessage.save()
            return Response(serializedMessage.data, status=status.HTTP_201_CREATED)
        return Response(serializedMessage.errors, status=status.HTTP_400_BAD_REQUEST)