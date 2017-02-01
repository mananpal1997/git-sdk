from urllib2 import HTTPSHandler, Request, build_opener
import json
import base64
import urllib

methods = ["GET", "POST", "PUT"]
URL = "https://api.github.com"


class QueryHook(object):
	def __init__(self, instance, query, method = None):
		self.instance = instance
		self.query = query
		self.method = method

	def __call__(self, *args, **kwargs):
		if self.method:
			return self.instance.http_call(self.method, self.query, **kwargs)
		if len(args) == 0:
			return self
		query = self.query + "/" + "/".join([arg for arg in args])
		return QueryHook(self.instance, query, self.method)

	def __getattr__(self, attr):
		if attr.upper() in methods:
			self.method = attr.upper()
			return QueryHook(self.instance, self.query, self.method)
		query = self.query + "/" + attr
		return QueryHook(self.instance, query, self.method)


class Github(object):
	def __init__(self, username, password):
		self.username = username
		self.password = password
		auth = base64.b64encode(bytes('%s:%s' % (username, password)), 'utf-8').decode('ascii')
		self.authorization = "Basic %s" % auth

	def __getattr__(self, attr):
		return QueryHook(self, "/" + attr)

	def http_call(self, method, query, **kw):
		data = None
		if method in ["POST", "PUT"]:
			data = json.dumps(kw)
		url = URL + query
		opener = build_opener(HTTPSHandler)
		req = Request(url, data)
		req.get_method = lambda: method
		req.add_header('Authorization', self.authorization)
		req.add_header('Content-Type', 'application/x-www-form-urlencoded')
		res = opener.open(req, timeout = 60)
		try:
			res = opener.open(req, timeout = 60)
			return res.read().decode('utf-8')
		except:
			print "Error"
			return