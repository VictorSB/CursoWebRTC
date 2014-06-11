from google.appengine.ext import webapp

#Routes
routes = [
    #Main Routes
      webapp.Route('/ej/<number>', 'controllers.main_controller.MainHandler'),
]

app = webapp.WSGIApplication(routes=routes, debug=True, config={})