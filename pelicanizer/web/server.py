import pkg_resources

from twisted.web import server, static

from pelicanizer.reactive import ReactiveMixin


class WebServer (ReactiveMixin):
    StaticDir = pkg_resources.resource_filename('pelicanizer', 'web/static')

    def __init__(self, reactor):
        ReactiveMixin.__init__(self, reactor)

        self._site = server.Site(static.File(self.StaticDir))
        self._site.displayTracebacks = False

    def listen(self, port):
        self._log.info(
            'Listening on port %r; static dir %r',
            port,
            self.StaticDir)
        self._reactor.listenTCP(port, self._site)
