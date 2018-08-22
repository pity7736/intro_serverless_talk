import datetime
import os
from uuid import uuid4

from pynamodb.attributes import UnicodeAttribute, UTCDateTimeAttribute, ListAttribute, MapAttribute
from pynamodb.models import Model


class Talk(Model):
    id = UnicodeAttribute(hash_key=True)
    when = UTCDateTimeAttribute(range_key=True)
    description = UnicodeAttribute(null=True)
    speakers = ListAttribute(of=MapAttribute)
    sponsors = ListAttribute(of=MapAttribute)
    city = UnicodeAttribute()

    class Meta:
        table_name = os.environ['DYNAMO_TALK_TABLE']
        host = os.environ['DYNAMO_HOST']
        write_capacity_units = 1
        read_capacity_units = 1
        region = 'us-east-1'

    def save(self, *args, **kwargs):
        if self.id is None:
            self.id = str(uuid4())
        if type(self.when) is str:
            self.when = datetime.datetime.strptime(self.when, '%Y-%m-%dT%H:%M:%S')
        super().save(*args, **kwargs)
