import os

import webapp2
import jinja2
import cgi


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape']
)


class MainPage(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('play.html')
        self.response.out.write(template.render())


class Rot13(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('rot13.html')
        context = {
            'text_value': ""
        }
        self.response.out.write(template.render(context))

    def post(self):
        template = JINJA_ENVIRONMENT.get_template('rot13.html')
        context = {
            'text_value': cgi.escape(rot13(self.request.get('text')))
        }
        self.response.out.write(template.render(context))


def rot13(string):
    result = ''
    for c in string:
        if not c.isalpha():
            result += c
            continue

        if ord(c) >= ord('A') and ord(c) <= ord('Z'):
            c13 = ord(c) + 13
            if c13 > ord('Z'):
                c13 -= 26
            result += chr(c13)
        elif ord(c) >= ord('a') and ord(c) <= ord('z'):
            c13 = ord(c) + 13
            if c13 > ord('z'):
                c13 -= 26
            result += chr(c13)
    return result


application = webapp2.WSGIApplication([
    ('/', Rot13),
], debug=True)
