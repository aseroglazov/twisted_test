import os

from twisted.web.static import File

from .api import api

root = File(os.path.join(os.path.dirname(__file__), 'static'))
root.putChild('api', api)
