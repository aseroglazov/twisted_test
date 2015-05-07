from twisted.web.server import Site
from twisted.internet import reactor

from .url_tree import root


def start(port=8080):
    reactor.listenTCP(port, Site(root))
    reactor.run()


def stop():
    reactor.callFromThread(reactor.stop)


if __name__ == '__main__':
    start_server()
