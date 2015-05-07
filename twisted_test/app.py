from twisted.web.server import Site
from twisted.internet import reactor

from .url_tree import root


def start():
    reactor.listenTCP(8080, Site(root))
    reactor.run()


def stop():
    reactor.callFromThread(reactor.stop)


if __name__ == '__main__':
    start_server()
