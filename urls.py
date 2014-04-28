import pages
urls=[
		(r'/',pages.IndexHandler),
		(r'/login', pages.LoginHandler),
		(r'/logout',pages.LogoutHandler),
		(r'/upload',pages.UploadHandler),
		(r'/(.*)',pages.UrlHandler),
	]

