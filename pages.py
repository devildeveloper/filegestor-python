import tornado.web

from settings import settings
from database import File,User, session

class IndexHandler(tornado.web.RequestHandler):
	def get(self):
		self.render('index.html')

class LoginHandler(tornado.web.RequestHandler):
	def get(self):
		self.render('login.html')
	def post(self):
		flag =False
		users=session().query(User).all()#hago la consulta a la base de datos
		if(len(users) > 0):
			for dato in users :
				if dato.name == self.get_argument("user") and dato.passw==self.get_argument("pass"):					
					self.render('user.html',user=self.get_argument("user"),user_id=dato.id)
					break		
		else:
			self.redirect('/')

class LogoutHandler(tornado.web.RequestHandler):
	def get(self):
		self.clear_cookie("user")
		self.redirect(self.get_argument("next", "/"))

class UploadHandler(tornado.web.RequestHandler):
	def post(self):		
		file1 = self.request.files['file'][0]
		original_fname = file1['filename']
		user=self.get_argument("user")#nombre de usuario
		user_id=self.get_argument("user_id")#id de usuario
		output_file = open("uploads/"+user+"/" + original_fname, 'wb')
		output_file.write(file1['body'])
		#bbdd
		_file=File(name=original_fname,user_id=int(user_id))
		session().add(_file)
		session().commit()
		self.finish("file " + original_fname + " is uploaded")		
	
			#self.write('error inesperado :s')	

#class FileHanlder(tornado.web.RequestHandler):
#	def get(self):
