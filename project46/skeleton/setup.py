try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup
		
config = {
	'description': 'MyProject',
	'author': 'Nitin Kumar',
	'url': 'URL to get it at.', 
	'download_url': 'Where to download it',
	'author_email': 'Nitin.kumar56@gmail.com',
	'version': '0.1',
	'install_requires':['nose'],
	'packages': ['NAME'],
	'scripts':[],
	'name': 'projectname'
}
setup(**config)			
