import http.server
from os import curdir, sep
import socketserver
import sys

DEFAULT_PORT = 8080

class mHandler(http.server.BaseHTTPRequestHandler):

	def do_HEAD(self):
		self.write_html_header()
		return

	def do_GET(self):
		try:
			if self.path.endswith('.html'):
				f = open(curdir + sep + self.path)
				self.write_html_header()
				#write to output stream from .html file
				#encode string to utf-8 charset as Python 3.x IO expects bytes
				self.wfile.write(f.read().encode('utf-8'))
				f.close()
				return
			else:
				self.write_html_header()
				#write standard greeting to output stream
				#encode string to utf-8 charset as Python 3.x IO expects bytes
				self.wfile.write('Hello World!'.encode('utf-8'))
				return
		except IOError:
			self.send_error(404, 'File Not Found: %s' % self.path)

	# from http://stackoverflow.com/questions/4233218/python-basehttprequesthandler-post-variables
	def do_POST(self):
		ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
		#parse form
		if ctype == 'multipart/form-data':
			post_params = cgi.parse_multipart(self.rfile, pdict)
			resolve_post_form(post_params)
        #parse url
		elif ctype == 'application/x-www-form-urlencoded':
			length = int(self.headers.getheader('content-length'))
			post_params = cgi.parse_qs(self.rfile.read(length), keep_blank_values=1)
			resolve_post_url(post_params)
		#nothing to parse
		else:
			post_params = {}
		self.send_response(301)
		return

	def resolve_post_form(self, form_params):
		#do fancy stuff here with form data
		pass

	def resolve_post_url(self, url_params):
		#do fancy stuff here with url data
		pass


	def write_html_header(self):
		self.send_response(200)
		self.send_header('Content-type', 'text/html')
		self.end_headers()
		return

def httpd(args=sys.argv):
	try:
		#grab port from cmd line
		port = DEFAULT_PORT if len(args) < 1 else int(args[1])
		server = http.server.HTTPServer(('', port), mHandler)
		print('Running HTTP Server on Port', port)
		server.serve_forever()
	except KeyboardInterrupt:
		print('Shutting Down Server...')
		server.socket.close()

#entry point
if __name__ == '__main__':
	httpd()