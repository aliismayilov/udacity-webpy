import os

import webapp2
import jinja2

from validators import valid_username, valid_password, valid_email, verify_password


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True
)


class MainPage(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('templates/play.html')
        self.response.out.write(template.render())


class WelcomePage(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('templates/welcome.html')

        context = {
            'username': self.request.get("u")
        }

        self.response.out.write(template.render(context))


class SignupHandler(webapp2.RequestHandler):
    def get(self, context={}):
        template = JINJA_ENVIRONMENT.get_template('templates/signup.html')
        self.response.out.write(template.render(context))
    def post(self):
        template = JINJA_ENVIRONMENT.get_template('templates/signup.html')

        context = { }
        error = False
        
        # username validation
        if not self.request.get("username"):
            context['username_error'] = 'Username is required'
            error = True
        elif not valid_username(self.request.get("username")):
            context['username_error'] = 'Username is not valid'
            context['username'] = self.request.get("username")
            error = True
        else:
            context['username'] = self.request.get("username")

        # password validation
        if not self.request.get("password"):
            context['password_error'] = 'Password is required'
            error = True
        elif not valid_password(self.request.get("password")):
            context['password_error'] = 'Password is not valid'
            error = True
        elif not verify_password(self.request.get("password"), self.request.get("verify")):
            context['password_error'] = "Passwords don't match"
            error = True

        # email validation
        if self.request.get("email") and not valid_email(self.request.get("email")):
            context['email_error'] = 'Email is not valid'
            context['email'] = self.request.get("email")
            error = True
        elif self.request.get("email"):
            context['email'] = self.request.get("email")

        if error:
            self.get(context=context)
        else:
            self.redirect("/welcome?u=%s" % context['username'])


class Rot13(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('templates/rot13.html')
        context = {
            'text': ""
        }
        self.response.out.write(template.render(context))

    def post(self):
        template = JINJA_ENVIRONMENT.get_template('templates/rot13.html')
        text = self.request.get('text')
        if text:
            text = text.encode('rot13')

        context = {
            'text': text
        }
        self.response.out.write(template.render(context))


application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/signup', SignupHandler),
    ('/welcome', WelcomePage)
], debug=True)
