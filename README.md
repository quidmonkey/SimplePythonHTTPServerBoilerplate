SimplePythonHTTPServerBoilerplate
=================================

A simple HTTP Server written in Python 3.2.3

This server is designed to run locally on the port of your choice:
```python
python server.py 80
```
If no port is specified, the server will default to port 8080.

If a specific .html file is requested, the server will serve it up; otherwise, the server will serve up a generic 'Hello World!' message. Additional GET requests on specific filetypes can be added like so:
```python
if self.path.endswith('.ext'):
	#serve up GET request here
```

The server is also designed to take form & url-encoded POST requests. The resolve_post_form() and resolve_post_url() methods can be overloaded with the desired logic.

Feel free to fork and improve as you see fit.

Enjoy!