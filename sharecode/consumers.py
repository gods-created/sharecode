from channels.generic.websocket import AsyncWebsocketConsumer
from json import loads, dumps, JSONDecodeError
from celery.result import AsyncResult
from asgiref.sync import sync_to_async

class CodeShareConsumer(AsyncWebsocketConsumer):
    CHANNEL_GROUP = None
    ROOM = None

    @sync_to_async
    def _is_task_ready(self, task_id: str) -> bool:
        result = AsyncResult(id=task_id)
        return result is None or result.ready()

    async def connect(self):
        self.ROOM = self.scope['url_route']['kwargs']['room']
        self.CHANNEL_GROUP = f'sharecode_room_{self.ROOM}'

        await self.channel_layer.group_add(
            self.CHANNEL_GROUP,
            self.channel_name
        )
        return await self.accept()
    
    async def disconnect(self, code: int = 0):
        return await self.channel_layer.group_discard(
            self.CHANNEL_GROUP,
            self.channel_name
        )
    
    async def receive(self, text_data: str = None, bytes_data: bytes = None):
        json_data = None 

        try:
            json_data = loads(text_data) if text_data else {}
            value, block = json_data.get('value'), json_data.get('block')
            task_kwargs = {
                'room_number': self.ROOM,
                'code': value if 'code' in block else '',
                'output': value if 'output' in block else '',
            }
            
            # is_ready = await self._is_task_ready(self.CHANNEL_GROUP)
            # if is_ready:
            from content.tasks import write_content

            write_content.apply_async(
                kwargs=task_kwargs,
                queue='high_priority',
                task_id=self.CHANNEL_GROUP
            )
        
        except JSONDecodeError:
            json_data = {}

        json_data['type'] = 'send_message'

        return await self.channel_layer.group_send(
            self.CHANNEL_GROUP,
            json_data
        )
    
    async def send_message(self, json_data: dict = None, bytes_data: bytes = None):
        return await self.send(
            dumps(json_data) if json_data else {}
        )