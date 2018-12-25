import tornado.web
from views import index

class Application(tornado.web.Application):
    def __init__(self):
        handlers=[
            (r'/',index.IndexHandler)
        ]

        #调用父类的Application  传入handlers
        super(Application,self).__init__(handlers)