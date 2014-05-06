import pages
urls=[
		(r'/',pages.IndexHandler),
		(r'/login', pages.LoginHandler),
		(r'/logout',pages.LogoutHandler),
		(r'/upload',pages.UploadHandler),
		(r'/getfiles',pages.GetMyFiles),
		(r'/perfil',pages.Perfil),
		(r'/(.*)',pages.UrlHandler),
	]

