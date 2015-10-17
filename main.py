import webapp2
import fitlanecal as fl

class MainPage(webapp2.RequestHandler):
    def get(self):
        cal = fl.get_calendar_at_club('Nice Centre')
        self.response.write(cal)

app = webapp2.WSGIApplication([('/', MainPage)], debug=True)


