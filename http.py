#!/usr/bin/env python
# encoding: utf-8
"""
Created by Ben Scott on '08/03/2016'.
"""

import SimpleHTTPServer
import SocketServer

PORT = 8001

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

print "serving at port", PORT
httpd.serve_forever()