

import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options
#1.基础方法  定义2个参数

tornado.options.define(name="port",default=8000,type=int,help="This is a port",
                       metavar=None,multiple=False,group=None,callback=None)
'''
type     变量类型 从命令行或配置导入参数值  如果没有设置type,则按default的类型.如果没有default,则不转换
multiple 设置选项变量是否为多个值,默认为False(比如穿列表)
help     变量的提示信息,一般不用
'''
tornado.options.define('list',default=[],type=str,multiple=True)

#2.属性   全局的options对象,所有定义的选项变量都会作为该对象的属性
tornado.options.options

#3.获取参数的方法  转换命令行参数
#tornado.options.parse_command_line()

class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write('Hsingpu is a good man')
    def post(self, *args, **kwargs):
        pass


if __name__ == '__main__':
    tornado.options.options.logging = None
    tornado.options.parse_config_file(path='config')  #从配置文件读取

    print('list=',tornado.options.options.list)
    app = tornado.web.Application([
        (r"/",IndexHandler)
    ])

    httpServer=tornado.httpserver.HTTPServer(app)

    httpServer.bind(tornado.options.options.port)
    httpServer.start(1)
    tornado.ioloop.IOLoop.current().start()

#不建议使用以上方式, 因为书写格式仍然需要安装python的语法要求  2.不支持字典类型
#最终版本 创建一个名为config.py的普通文件,当做模块来用