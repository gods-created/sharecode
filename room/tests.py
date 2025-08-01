from django.test import TestCase
from unittest.mock import patch
from .models import Room
from .serializers import RoomSerializer

class RoomTests(TestCase):
    @patch('room.models.Room.objects.filter')
    def test_filter_room_with_mock(self, mock):
        mock.return_value = None 
        response = Room.objects.filter(number=1)
        mock.assert_called_once_with(number=1)
        self.assertIsNone(response) 

    @patch.object(RoomSerializer, 'create_room')
    def test_serializer_with_mock(self, mock):
        mock.return_value = {}
        serializer = RoomSerializer(data={})
        response = serializer.create_room()
        mock.assert_called_once_with()
        self.assertIsInstance(response, dict) 

    def test_create_room_api(self):
        request = self.client.get('/api/create_room/')
        status = request.status_code
        response = request.json()
        self.assertEqual(status, 201)
        self.assertIn('number', response)
        self.assertEqual(len(str(response['number'])), 9)