from django.db.models import (
    Model,
    TextField,
    Index,
    OneToOneField,
    CASCADE
)

class Content(Model):
    room = OneToOneField('room.Room', related_name='content', null=False, on_delete=CASCADE)
    code = TextField(null=False, blank=True, default='')
    output = TextField(null=False, blank=True, default='')

    class Meta:
        app_label = 'content'
        db_table = 'contents'
        ordering = ['pk', 'room_id', 'code', 'output']
        indexes = (
            Index(fields=['room_id']),
        )

    def __str__(self):
        return 'Code: \'{0}\'. Output: \'{1}\'.'.format(self.code, self.output)