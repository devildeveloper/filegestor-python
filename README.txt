FILEGESTOR-PYtHON
-----------------------------------------------------

EL PROYECTO ESTA EN CONSTANTE DESARROLLO, AUN NO ESTA OPTIMIZADO

Nombre clave : DroPy
Licencia: Creative Commons(no comercial usage)

-----------------------------------------------------

Requisitos:

tornado
sqlalchemy

-----------------------------------------------------

Archivos:

*****************************************
*	create_user.py 						*
*****************************************
*	archivo para crear usuarios, crei 	*
*	mas seguro crear los usuarios por	*
*	medio de un script que por gestor	*
*	web.								*
*										*
*	Para usarlo solo ejecuten:			*
*										*
*	>>python create_user.py 			*
*										*
*	sigan las instrucciones que son :	*
*										*
*	1-introducir el nombre del usuario 	*
*	2-crear una clave 					*
*										*
*	el script creara al usuario con y	*
*	la clave, tambien creara una nueva 	*
*	carpeta con el nombre del usuario 	*
*	dentro del directorio "uploads", 	*
*	en ese directorio es donde se 		*
*	suben los archivos que el usuario 	*
*	almacena.							*
*										*
*****************************************

°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
°	database.py 						°
°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
° 	Archivo donde se definen los models	°
° 	que se usaran en el proyecto, esta	°
° 	en constante observacion y			°
° 	desarrollo.							°
° 	Las clases User y File son las 		°
° 	unicas creadas hasta el momento y	°
° 	las unicas usadas en el proyecto	°
° 										°
°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°

-----------------------------------------
|	urls.py 							|
|----------------------------------------
|	archivo donde se definen las urls 	|
|	y sus controladores(clases creadas 	|
|	en pages.py).						|
| 										|
|----------------------------------------
|	pages.py 							|
|----------------------------------------
|	Aqui se crean los handlers 			|
|	(controladores) que responden al 	|
|	llamado de urls.py . 				|
| 										|
|	cada clase cuenta con un metodo 	|
|	get y post el cual reacciona 		|
|	segun el evento de formulario que 	|
|	lo invoque. 						|
| 										|
|----------------------------------------
|	main.py 							|
|----------------------------------------
| 										|
|	archivo principal del proyecto. 	|
|	Aqui se crea la instanci de 		|
|	tornado que le da vida al 			|
|	proyecto  							|
|										|
-----------------------------------------
