import os.path

import tornado.ioloop
import tornado.web
import tornado.httpserver
import tornado.options

import urls
import settings

from tornado.options import define , options
define("port",default =8888 , help="run on the given port ", type=int)
if __name__ == "__main__":
	tornado.options.parse_command_line()
	app=tornado.web.Application(
		handlers=urls.urls,
		template_path=settings.template_path,
		static_path=settings.static_path,
		debug=True
	)
	http_server=tornado.httpserver.HTTPServer(app)
	http_server.listen(options.port)
	tornado.ioloop.IOLoop.instance().start()
