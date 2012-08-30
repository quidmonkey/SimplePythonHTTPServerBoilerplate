SimplePythonHTTPServerBoilerplate Changelog
===========================================

##v1.1.1
- Fixed do_POST() to parse from the headers dictionary and updated cgi.parse_qs() (deprecated) to urllib.parse.parse_qs

##v1.1
- Re-factored do_GET() to allow for any GET request of known MIME type.
- Added Favicon error handling.
- Added DocString.