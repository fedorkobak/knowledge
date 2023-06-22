def application(environ, start_response):
    status = '200 OK'
    output = b"I'm application from /subulr. Basic example of wsgi"

    response_headers = [('Content-type', 'text/plain'),
                        ('Content-Length', str(len(output)))]
    start_response(status, response_headers)

    return [output]