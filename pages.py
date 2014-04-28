import tornado.web

from settings import settings

import datos

class IndexHandler(tornado.web.RequestHandler):
	def get(self):
		self.render('index.html')

class LoginHandler(tornado.web.RequestHandler):
	def get(self):
		self.render('login.html')
	def post(self):
		flag = False;
		for  dato  in datos.datos :
			if dato['user'] == self.get_argument("user"):				
				flag=True
		if flag == True :
			self.render('user.html',user=self.get_argument("user"))
		else:
			self.write('no valido')

class LogoutHandler(tornado.web.RequestHandler):
	def get(self):
		self.clear_cookie("user")
		self.redirect(self.get_argument("next", "/"))

class UploadHandler(tornado.web.RequestHandler):
	def post(self):
		file1 = self.request.files['file'][0]
		original_fname = file1['filename']
		user=self.get_argument("idol")
		output_file = open("uploads/"+user+"/" + original_fname, 'wb')
		output_file.write(file1['body'])

		self.finish("file " + original_fname + " is uploaded")