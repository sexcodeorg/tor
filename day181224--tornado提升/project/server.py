import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options
import config
from views   import index
from application import Application



if __name__ == '__main__':

    # ])#独立视图
    app=Application()
    httpServer = tornado.httpserver.HTTPServer(app)
    # 直接调用配置文件中的
    httpServer.bind(config.options['port'])
    httpServer.start(1)
    tornado.ioloop.IOLoop.current().start()

