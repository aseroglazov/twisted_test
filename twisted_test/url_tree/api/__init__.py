from twisted.web.resource import Resource

from .images import images


api = Resource()
api.putChild('images', images)
