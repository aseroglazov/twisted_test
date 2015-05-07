import json

from cStringIO import StringIO
from PIL import Image
from tempfile import mkstemp

from twisted.web.resource import Resource, NoResource

from twisted_test.db import ImageStorage
from twisted_test.tools import download_file

from .actions import FlipPage


KNOWN_ACTIONS = {'flip': FlipPage}


class AddPage(Resource):
    def render_POST(self, request):
        try:
            input_image = Image.open(StringIO(request.args['image'][0]))
        except Exception, e:
            id = None
            success = False
            error = 'Unsupported image type'
        else:
            stored_image = ImageStorage()
            stored_image.format=input_image.format.lower()
            stored_image.content.put(
                StringIO(request.args['image'][0]),
                content_type='image/{}'.format(stored_image.format)
            )
            stored_image.save()


            id = stored_image.id
            success = True
            error = None

        return json.dumps(
            {
                'success': success,
                'data': {'id': id},
                'error': error
            }
        )


class StoredImagePage(Resource):
    isLeaf = False

    def __init__(self, id):
        self.id = id
        self.children = {}

    def getChild(self, name, request):
        if name not in KNOWN_ACTIONS:
            return NoResource()

        return KNOWN_ACTIONS[name](ImageStorage.objects(id=self.id).first())

    def render_GET(self, request):
        image = ImageStorage.objects(id=self.id).first()

        _, tmp_file = mkstemp()
        with open(tmp_file, 'wb') as file:
            file.write(image.content.read())

        return download_file(
            request,
            'image.{}'.format(image.format),
            tmp_file,
            file_is_temp=True
        )


class GetPage(Resource):
    def getChild(self, id, request):
        if not ImageStorage.objects(id=id):
            return NoResource()

        return StoredImagePage(id)
