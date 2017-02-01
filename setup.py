from setuptools import setup

requires = []

setup(
	name = "git_sdk",
	py_modules = ["git_sdk"],
	version = "0.1.0",
	description = "Github API SDK",
	author = "Manan Pal",
	author_email = "mananpal42@gmail.com",
	keywords = ["github"],
	url = "https://github.com/mananpal1997/git-sdk",
	install_requires = requires,
	long_description = "A python SDK for Github API",
	classifiers = [
					"Programming Language :: Python",
        			"Operating System :: OS Independent",
        			'Intended Audience :: Developers',
			        'Programming Language :: Python',
			        'Programming Language :: Python :: 2.7'
				]
)