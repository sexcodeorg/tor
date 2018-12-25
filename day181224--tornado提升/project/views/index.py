import tornado.web
from tornado.web import RequestHandler

class IndexHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.write('Hsingpu is a good man')

    def post(self, *args, **kwargs):
        pass