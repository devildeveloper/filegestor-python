#este script solo corre por linea de comandos
import os
from getpass import getpass
from database import User,File,session

user_name = raw_input('ingrese el nombre de usuario ')
user_pass = getpass('ingrese la clave de usuario ')
confirm = raw_input('confirma creacion?(s/n) ')
if confirm == 's' :
	try:
		d=User(name=user_name,passw=user_pass)
		s=session()
		s.add(d)
		s.commit()
		os.system('mkdir uploads/'+user_name)
		print('directorio creado con exito')
	except :
		print('no se pudo crear el directorio')
else :
	print('operacion cancelada')


