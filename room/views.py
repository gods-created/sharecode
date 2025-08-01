from rest_framework import status
from rest_framework.response import Response
from adrf.decorators import api_view
from asgiref.sync import sync_to_async
from .serializers import RoomSerializer
from content.serializers import ContentSerializer

@api_view(http_method_names=['GET'])
async def create_room(request) -> Response:
    data = request.data
    serializer = RoomSerializer(data=data)
    await sync_to_async(serializer.is_valid)(raise_exception=True)
    room = await sync_to_async(serializer.create_room)()
    return Response(
        status=status.HTTP_201_CREATED,
        data=room
    )

@api_view(http_method_names=['POST'])
async def room_content(request) -> Response:
    data = request.data
    serializer = ContentSerializer(data=data)
    await sync_to_async(serializer.is_valid)(raise_exception=True)
    room = await sync_to_async(serializer.room_content)()
    return Response(
        status=status.HTTP_200_OK,
        data=room
    )