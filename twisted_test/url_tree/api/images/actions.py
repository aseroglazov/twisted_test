from cStringIO import StringIO
from PIL import Image
from tempfile import mkstemp

from twisted.web.resource import Resource

from twisted_test.tools import download_file


class FlipPage(Resource):
    def __init__(self, image):
        self.image = image

    def render_GET(self, request):
        image = Image.open(self.image.content)
        flipped = image.transpose(Image.FLIP_TOP_BOTTOM)
        _, tmp_file = mkstemp(suffix='.{}'.format(self.image.format))
        flipped.save(tmp_file, self.image.format)

        return download_file(
            request,
            'flipped.image.{}'.format(self.image.format),
            tmp_file,
            file_is_temp=True
        )
