import tornado.web
from database import File,User, session
import datetime 
from tornado import httpclient 
import os
import json

class IndexHandler(tornado.web.RequestHandler):
	def post(self):
		self.redirect('/')
	def get(self):
		try:
			user=self.get_secure_cookie("user")		
			data=json.loads(user)	
			s=session()		
			if(s.query(User).filter(User.id==int(data['user_id']),User.name==data['user'].encode('utf8'),User.status==1).count() == 1):
				self.render('user.html',user=data['user'],user_id=data['user_id'])
		except:			
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
					vjson={'user_id':dato.id,'user':dato.name}					
					#print json.dumps({'user_id':dato.id,'user':dato.name},sort_keys=True,indent=4)
					self.set_secure_cookie("user", json.dumps(vjson))
					self.render('user.html',user=dato.name,user_id=dato.id)
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
		if len(die) == 0 :
			die=(datetime.datetime.utcnow()+datetime.timedelta(weeks=1)).date()		
		#bbdd
		_file=File(name=original_fname,user_id=int(user_id),expiration=die)
		s=session()
		s.add(_file)
		s.commit()
		s.close()
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
					q2=s.query(File).filter(File.user_id==q1[0].id,File.name==arch)
					if(q2.count() > 0):
						if(q2[0].expiration > datetime.date.today()):
							_file_dir = os.path.abspath("")+"/uploads/"+user
							_file_path = "%s/%s" % (_file_dir, arch)
							if not arch or not os.path.exists(_file_path):
								raise httpclient.HTTPError(404)
							self.set_header('Content-Type', 'application/force-download')
							self.set_header('Content-Disposition', 'attachment; filename=%s' % arch)
							with open(_file_path, "rb") as f:
								try:
									while True:
										_buffer = f.read(4096)
										if _buffer:
											self.write(_buffer)
										else:
											f.close()
											self.finish()
											return
								except:
									raise httpclient.HTTPError(404)
							raise httpclient.HTTPError(500)
						else:
							self.write('expired link')
					else:
						self.write('invalid file')
				else:
					self.write('invalid user')			
			else:
				self.write('invalids params')	
class GetMyFiles(tornado.web.RequestHandler):
	#def get(self):
	#	self.write('no autorizado')
	def get(self):
		user=self.get_secure_cookie("user")		
		data=json.loads(user)	
		s=session()		
		if(s.query(User).filter(User.id==int(data['user_id']),User.name==data['user'].encode('utf8'),User.status==1).count() == 1):
			_files=s.query(File).filter(File.user_id==data['user_id'],File.status==1).all()
			self.render('user-files.html',user=data['user'],files=_files)

class Perfil(tornado.web.RequestHandler):
	def post(self):
		self.write('no se porque estas viendo esto..')
	def get(self):
		try:
			user=self.get_secure_cookie("user")		
			data=json.loads(user)	
			s=session()		
			if(s.query(User).filter(User.id==int(data['user_id']),User.name==data['user'].encode('utf8'),User.status==1).count() == 1):
				self.render('user.html',user=data['user'],user_id=data['user_id'])		
		except:
			self.redirect('/')