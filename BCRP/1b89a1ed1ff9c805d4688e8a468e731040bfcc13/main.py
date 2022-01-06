# Copyright 2011 Digital Inspiration
# http://www.labnol.org/

import os
import webapp2
from google.appengine.ext.webapp import template

class MainHandler(webapp2.RequestHandler):
  def get (self, q):
    if q is None:
      q = 'index.html'
     
    if q == 'index.html':
      self.redirect('http://ehhapp.org', permanent=True)

    path = os.path.join (os.path.dirname (__file__), q)
    self.response.headers ['Content-Type'] = 'text/html'
    self.response.out.write (template.render (path, {}))

app = webapp2.WSGIApplication([('/(.*html)?', MainHandler)])
