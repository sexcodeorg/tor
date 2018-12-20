

import tornado.web
import tornado.ioloop

#类比django中的视图   习惯用法加上Handler
class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write('Hsingpu is a good man')
    def post(self, *args, **kwargs):
        pass


if __name__ == '__main__':
    #实例化应用对象   Application: 是tornado web框架的核心应用类 ,是与服务器对应的接口 里面保存了路由映射表
    #有一个listen方法创建了一个http服务器示例 并绑定了端口
    app = tornado.web.Application([
        (r"/",IndexHandler)
    ])
    app.listen(8000)
    '''IOLoop.current()
    返回当前线程的IOLoop实例
    .start():启动IOLoop实例的I/O循环
    '''
    tornado.ioloop.IOLoop.current().start()