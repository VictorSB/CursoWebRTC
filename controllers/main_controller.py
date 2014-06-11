from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
import os


class MainHandler(webapp.RequestHandler):
    def get(self, number):
        t_path = '../ej'+str(number)+'.html'
        path = os.path.join(os.path.dirname(__file__), t_path)
        self.response.out.write(template.render(path, {}))