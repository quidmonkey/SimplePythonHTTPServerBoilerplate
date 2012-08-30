import http.server
import mimetypes
from os import curdir, sep
import socketserver
import sys
from urllib.parse import parse_qs

DEFAULT_PORT = 8080

#blank favicon gif
BLANK_FAVICON = 'GIF89a\x01\x00\x01\x00\xf0\x00\x00\xff\xff\xff\x00\x00\x00!\xff\x0bXMP DataXMP\x02?x\x00!\xf9\x04\x05\x00\x00\x00\x00,\x00\x00\x00\x00\x01\x00\x01\x00@\x02\x02D\x01\x00;'

class mHandler(http.server.BaseHTTPRequestHandler):

	def do_GET(self):
		# from https://github.com/amadeus/python-impact/blob/master/server.py
		try:
			#isolate file name - remove url-encoding
			file_path = self.path.split('?', 1)[0]

			#remove the leading forward slash
			if file_path[0] == '/':
				file_path = file_path[1:]

			#security, remove the ..
			file_path = file_path.replace('..', '')

			#determine the full path
			file_path = curdir + sep + file_path

			#grab data as bytes
			data = open(file_path, 'rb').read()

			#grab MIME type
			type, _ = mimetypes.guess_type(file_path)

			#write header
			self.send_response(200)
			self.send_header('Content-Type', type)
			self.send_header('Content-Length', len(data))
			self.end_headers()

			#write response
			self.wfile.write(data)

		except IOError:
			#prevent favicon errors
			if sep + 'favicon.ico' in file_path:
				self.send_response(200)
				self.send_header('Content-Type', 'image/gif')
				self.wfile.write(BLANK_FAVICON.encode('utf-8'))
				self.end_headers()
			else:
				self.send_error(404, 'File Not Found: %s' % file_path )

	#evolved from http://stackoverflow.com/questions/4233218/python-basehttprequesthandler-post-variables
	def do_POST(self):
		ctype, pdict = cgi.parse_header(self.headers['content-type'])
		#parse form
		if ctype == 'multipart/form-data':
			post_params = cgi.parse_multipart(self.rfile, pdict)
			resolve_post_form(post_params)
		#parse url
		elif ctype == 'application/x-www-form-urlencoded':
			length = int(self.headers['content-length'])
			post_params = parse_qs(self.rfile.read(length), keep_blank_values = True)
			resolve_post_url(post_params)

		self.send_response(301)
		return

	def resolve_post_form(self, form_params):
		'''Resolves POST request from a form'''
		#do fancy stuff here with form data
		pass

	def resolve_post_url(self, url_params):
		'''Resolves URL-encoded POST request'''
		#do fancy stuff here with url data
		pass

	def __repr__(self):
		return 'A simple HTTP server written in Python 3.2.3. Capable of GET and POST requests.'

def httpd(args=sys.argv):
	try:
		#grab port from cmd line
		port = DEFAULT_PORT if len(args) < 2 else int(args[1])
		server = http.server.HTTPServer(('', port), mHandler)
		print('Running HTTP Server on Port', port)
		server.serve_forever()
	except KeyboardInterrupt:
		print('Shutting Down Server...')
		server.socket.close()

#entry point
if __name__ == '__main__':
	httpd()