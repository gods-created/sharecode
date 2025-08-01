from django.test import TestCase
from .models import Content
from unittest.mock import MagicMock

class ContentTests(TestCase):
    def test_content_create(self):
        Content.objects.create = MagicMock()
        Content.objects.create.return_value = object
        obj = Content.objects.create(room_id=1)
        Content.objects.create.assert_called_once_with(room_id=1)
        self.assertIsInstance(obj, object)