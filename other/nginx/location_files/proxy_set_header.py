import http.server
import socketserver

class RequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Server received your GET request\n")
        self.wfile.write(b"Raw request data:\n\n")
        self.wfile.write(self.raw_requestline)
        self.wfile.write(b"\nHeaders:\n")
        self.wfile.write(bytes(str(self.headers), "utf-8"))

PORT = 7890
with socketserver.TCPServer(("", PORT), RequestHandler) as httpd:
    print("Serving at port", PORT)
    httpd.serve_forever()
