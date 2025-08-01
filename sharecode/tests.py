from channels.testing import WebsocketCommunicator
from .asgi import application
from django.test import TestCase
from faker import Faker

class CodeShareConsumerTests(TestCase):
    def setUp(self):
        faker = Faker()
        self.room = ''.join(faker.random_letters(length=25))
        self.data = {'value': 'hello', 'block': 'code'}
    
    async def test_consumer(self):
        communicator = WebsocketCommunicator(
            application=application,
            path=f'ws/code/{self.room}/'
        )

        await communicator.connect()
        await communicator.send_json_to(data=self.data)
        result = await communicator.receive_json_from()
        await communicator.disconnect()

        self.assertIn('value', result)
        self.assertEqual(result['value'], 'hello')