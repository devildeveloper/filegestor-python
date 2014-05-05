#este script solo corre por linea de comandos
import os
from getpass import getpass
from database import User,File,session

user_name = raw_input('ingrese el nombre de usuario ')
user_pass = getpass('ingrese la clave de usuario ')
confirm = raw_input('confirma creacion?(s/n) ')
if confirm == 's' :
	#creacion del usuario
	try:		
		s=session()
		result=s.query(User).filter(User.name==user_name)
		if result.count() >0:
			print 'este usuario ya fue creado :('
		else :			
			d=User(name=user_name,passw=user_pass)
			s.add(d)
			s.commit()
			print('usuario creado con exito')
	except Exception as e:
		print(e)
	#creacion de su carpeta de uploads
	try:		
		if os.path.exists(os.path.join(os.getcwd(),'uploads')):
			print ' el directorio ya existe'
		else:			
			os.system('mkdir uploads/'+user_name)
			print('directorio creado con exito')		
	except Exception as e:
		print (e)
else:
	print('operacion cancelada')


