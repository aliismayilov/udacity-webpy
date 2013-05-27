import os

import webapp2
import jinja2


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True
)


class MainPage(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('play.html')
        self.response.out.write(template.render())


class Rot13(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('rot13.html')
        context = {
            'text': ""
        }
        self.response.out.write(template.render(context))

    def post(self):
        template = JINJA_ENVIRONMENT.get_template('rot13.html')
        text = self.request.get('text')
        if text:
            text = text.encode('rot13')

        context = {
            'text': text
        }
        self.response.out.write(template.render(context))


application = webapp2.WSGIApplication([
    ('/', Rot13),
], debug=True)
