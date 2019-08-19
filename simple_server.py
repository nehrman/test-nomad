# This Python file uses the following encoding: utf-8
import http.server
import socketserver
import os

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
   def end_headers(self):
        self.send_my_headers()
        http.server.SimpleHTTPRequestHandler.end_headers(self)

   def send_my_headers(self):
        self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")

with socketserver.TCPServer((os.environ['NOMAD_IP_toto'], int(os.environ['NOMAD_PORT_toto'])), MyHTTPRequestHandler) as httpd:
    httpd.serve_forever()

