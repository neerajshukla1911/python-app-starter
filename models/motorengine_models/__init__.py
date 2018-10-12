import tornado
from motorengine import connect

from config_reader import get_config

config = get_config('db')

io_loop = tornado.ioloop.IOLoop.instance()
connect(config['db_name'], host=config['host'], port=int(config['port']), io_loop=io_loop)  # you only need to keep track of the
                                                               # DB instance if you connect to multiple databases.