

import tornado.web
import tornado.ioloop
import tornado.httpserver
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
    #app.listen(8000)   #方法一    单进程模式
    #实例化一个http服务器对象 并 绑定端口
    httpServer=tornado.httpserver.HTTPServer(app)
    #httpServer.listen(8000)   #方法二  方法二拆分为下面方法三
    httpServer.bind(8000)
    httpServer.start(5)         #指定进程数 如为None或者小于等于0则根据cpu核心数进行创建
    '''IOLoop.current()
    返回当前线程的IOLoop实例
    .start():启动IOLoop实例的I/O循环
    '''
    tornado.ioloop.IOLoop.current().start()
    '''
    不用上述方式启动的问题   问题一:每个子进程都会从父进程中复制一份IOLoop的实例,如果在创建子进程前修改了IOLoop,会
    影响所有的子进程
    2.所有的进程都是由一个命令启动的(python  server.py),无法做到在不停止服务的情况下修改代码.
    3.所有进程共享一个端口,想要分别监控很困难
    '''