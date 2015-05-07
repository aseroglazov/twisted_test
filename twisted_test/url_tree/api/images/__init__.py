from twisted.web.resource import Resource

from .images import AddPage, GetPage


images = Resource()
images.putChild('add', AddPage())
images.putChild('get', GetPage())
