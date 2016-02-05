import webapp2
import fitlanecal as fl

CAL_EXT = '.ics'

class Provider_Cannes_Carnot(webapp2.RequestHandler):
    def get(self):
        cal = fl.get_calendar_at_club('cannes-carnot')
        self.response.write(cal)

        
class Provider_Cannes_Gare(webapp2.RequestHandler):
    def get(self):
        cal = fl.get_calendar_at_club('cannes-gare')
        self.response.write(cal)

        
class Provider_Cannes_La_Bocca(webapp2.RequestHandler):
    def get(self):
        cal = fl.get_calendar_at_club('cannes-la-bocca')
        self.response.write(cal)

        
class Provider_Juan_Les_Pins(webapp2.RequestHandler):
    def get(self):
        cal = fl.get_calendar_at_club('juan-les-pins')
        self.response.write(cal)

        
class Provider_Mandelieu(webapp2.RequestHandler):
    def get(self):
        cal = fl.get_calendar_at_club('mandelieu')
        self.response.write(cal)

        
class Provider_Nice_Centre(webapp2.RequestHandler):
    def get(self):
        cal = fl.get_calendar_at_club('nice-centre')
        self.response.write(cal)

        
class Provider_Nice_St_Isidore(webapp2.RequestHandler):
    def get(self):
        cal = fl.get_calendar_at_club('nice-st-isidore')
        self.response.write(cal)

        
class Provider_Sophia_Antipolis(webapp2.RequestHandler):
    def get(self):
        cal = fl.get_calendar_at_club('sophia-antipolis')
        self.response.write(cal)

        
class Provider_Villeneuve_Loubet(webapp2.RequestHandler):
    def get(self):
        cal = fl.get_calendar_at_club('villeneuve-loubet')
        self.response.write(cal)

        
class Provider_Villeneuve_A8(webapp2.RequestHandler):
    def get(self):
        cal = fl.get_calendar_at_club('villeneuve-A8')
        self.response.write(cal)

        
app = webapp2.WSGIApplication([('/cannes-carnot' + CAL_EXT, Provider_Cannes_Carnot),
                               ('/cannes-gare' + CAL_EXT, Provider_Cannes_Gare),
                               ('/cannes-la-bocca' + CAL_EXT, Provider_Cannes_La_Bocca),
                               ('/juan-les-pins' + CAL_EXT, Provider_Juan_Les_Pins),
                               ('/mandelieu' + CAL_EXT, Provider_Mandelieu),
                               ('/nice-centre' + CAL_EXT, Provider_Nice_Centre),
                               ('/nice-st-isidore' + CAL_EXT, Provider_Nice_St_Isidore),
                               ('/sophia-antipolis' + CAL_EXT, Provider_Sophia_Antipolis),
                               ('/villeneuve-loubet' + CAL_EXT, Provider_Villeneuve_Loubet),
                               ('/villeneuve-A8' + CAL_EXT, Provider_Villeneuve_A8)], debug=True)
