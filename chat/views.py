from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Room, Message
from .serializers import RoomSerializer, MessageSerializer

class HomeView(APIView):
    def get(self, request):
        return Response({"message": "Hello, world!"})

class RoomView(generics.RetrieveAPIView):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()
    lookup_field = 'name'

class CheckView(APIView):
    def post(self, request):
        room_name = request.POST.get('room_name')
        username = request.POST.get('username')

        if Room.objects.filter(name=room_name).exists():
            return Response({'message': 'Room already exists'})
        else:
            new_room = Room.objects.create(name=room_name)
            return Response({'message': 'Room created', 'room_id': new_room.id})

class MessageView(generics.ListCreateAPIView):
    serializer_class = MessageSerializer

    def get_queryset(self):
        room_name = self.kwargs['room']
        room = Room.objects.get(name=room_name)
        return Message.objects.filter(room=room.id)

    def perform_create(self, serializer):
        room_name = self.kwargs['room']
        username = self.request.data.get('username')
        room = Room.objects.get(name=room_name)
        serializer.save(user=username, room=room)

class MessageDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()
