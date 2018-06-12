# generate server.xml with the following command:
#    openssl req -new -x509 -keyout server.pem -out server.pem -days 365 -nodes
# run as follows:
#    python simple-https-server.py
# then in your browser, visit:
#    https://localhost:4443

#!/usr/bin/env python

from http.server import BaseHTTPRequestHandler, HTTPServer
import ssl

# HTTPRequestHandler class
class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):

    # GET
    def do_GET(self):
        # Send response status code
        self.send_response(200)

        # Send headers
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        # Send message back to client
        message = "Hello world!"
        # Write content as utf-8 data
        self.wfile.write(bytes(message, "utf8"))
        return

def run():
    print('starting server...')
    server_address = ('skyone.s7sky.com', 8081)
    httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)

    httpd.socket = ssl.wrap_socket (httpd.socket,
        keyfile="/home/eric/python/https_server/privkey.pem",
        certfile='/home/eric/python/https_server/fullchain.pem', server_side=True)
    httpd.serve_forever()


run()