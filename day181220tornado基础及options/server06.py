

import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options
import config


class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write('Hsingpu is a good man')
    def post(self, *args, **kwargs):
        pass


if __name__ == '__main__':
#直接调用配置文件中
    print('list=',config.options['list'])
    app = tornado.web.Application([
        (r"/",IndexHandler)
    ])

    httpServer=tornado.httpserver.HTTPServer(app)
#直接调用配置文件中的
    httpServer.bind(config.options['port'])
    httpServer.start(1)
    tornado.ioloop.IOLoop.current().start()

