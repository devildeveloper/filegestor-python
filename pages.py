import tornado.web

from settings import settings
from database import File,User, session
from datetime import date
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
		die=self.get_argument("datepicker")#fecha de expiracion
		output_file = open("uploads/"+user+"/" + original_fname, 'wb')
		output_file.write(file1['body'])
		#bbdd
		_file=File(name=original_fname,user_id=int(user_id),expiration=die)
		s=session()
		s.add(_file)
		s.commit()
		self.finish("file " + original_fname + " is uploaded")	
	
			#self.write('error inesperado :s')	
class UrlHandler(tornado.web.RequestHandler):
	def get(self,name):
		if not name:
			self.write('No params to read')
		else:
			path=name.split('/')
			if(len(path) == 2):
				user = name.split('/')[0]
				arch = name.split('/')[1]
				s=session()
				q1=s.query(User).filter(User.name==user)
				if(q1.count()==1):
					q2=s.query(File).filter(File.user_id==q1.id,File.name==arch)
					if(q2.count() == 1):
						if(q2.expiration < date.today()):
							dl=os.path.join(os.path.dirname(__file__), "uploads/",user,"/",arch)
							self.write(dl)
						else:
							self.write('expired link')
					else:
						self.write('invalid file')
				else:
					self.write('invalid user')			
			else:
				self.write('invalids params')	

#class FileHanlder(tornado.web.RequestHandler):
#	def get(self):
