import tornado.web

from jinja2 import Environment, FileSystemLoader, TemplateNotFound

import settings
import datos
env = Environment(loader=FileSystemLoader(settings.template_path))

class IndexHandler(tornado.web.RequestHandler):
	def get(self):
		template = env.get_template('index.html')
		self.write(template.render())

class LoginHandler(IndexHandler):
	def get(self):
		template = env.get_template('login.html')
		self.write(template.render())

	def post(self):
		flag = False;
		for  dato  in datos.datos :
			if dato['user'] == self.get_argument("user"):				
				flag=True
		if flag == True :
			template = env.get_template('user.html')
			self.write(template.render(user = self.get_argument("user"),static_url=settings.static_path))		
		else:
			self.write('no valido')

class LogoutHandler(IndexHandler):
	def get(self):
		self.clear_cookie("user")
		self.redirect(self.get_argument("next", "/"))

class UploadHandler(IndexHandler):
	def post(self):
		file1 = self.request.files['file'][0]
		original_fname = file1['filename']
		user=self.get_argument("idol")
		output_file = open("uploads/"+user+"/" + original_fname, 'wb')
		output_file.write(file1['body'])

		self.finish("file " + original_fname + " is uploaded")