from mongoengine import connect, Document, ObjectIdField, ImageField, StringField
from uuid import uuid4


connect('twisted_test')


class ImageStorage(Document):
    id = StringField(primary_key=True, default=str(uuid4()))
    content = ImageField()
    format = StringField()
