SimplePythonHTTPServerBoilerplate
=================================

A simple HTTP Server written in Python 3.2.3

This server is designed to run locally on the port of your choice:
```python
python server.py 80
```
If no port is specified, the server will default to port 8080.

The server is designed to take any GET request and POST request. The resolve_post_form() and resolve_post_url() methods are provided for a form and url-encoded POST respectively. Both should be overridden with the desired custom logic. It is important to note that the post_params will be passed in as bytes and may need to be decoded.

Feel free to fork and improve as you see fit.

Enjoy!

Special Thanks: I owe a great debt to the [Python-Impact](https://github.com/amadeus/python-impact/) Web Server. Much of the GET logic was taken from there. A big shout out to its author [Armon](https://github.com/armon).