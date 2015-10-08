import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'gaenv'))

import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello, World!')

app = webapp2.WSGIApplication([('/', MainPage)], debug=True)


