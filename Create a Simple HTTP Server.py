# -*- coding: utf-8 -*-
"""
Let’s Create a Simple HTTP Server 
https://www.afternerd.com/blog/python-http-server/
andare su http://localhost:8080/ 
serve file index.html 
@author: fabio
"""

import http.server
import socketserver

PORT = 8080
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
    

#-------------------------    
#FILE index.html 
#
#<html>
#    <head>
#        <title>Python is awesome!</title>
#    </head>
#    <body>
#        <h1>Afternerd</h1>
#        <p>Congratulations! The HTTP Server is working!</p>
#    </body>
#</html>
#-------------------------