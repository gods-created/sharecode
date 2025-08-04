from django.test import TestCase
from unittest.mock import patch
from .models import Room
from .serializers import RoomSerializer

class RoomTests(TestCase):
    def setUp(self):
        self.language = 'python'
    
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
        response = serializer.create_room(language=self.language)
        mock.assert_called_once_with(language=self.language)
        self.assertIsInstance(response, dict) 

    def test_create_room_api(self):
        request = self.client.post(
            path='/api/create_room/',
            data={
                'language': self.language
            }
        )
        status = request.status_code
        response = request.json()
        self.assertEqual(status, 201)
        self.assertIn('number', response)
        self.assertTrue(len(str(response['number'])) in [8, 9])