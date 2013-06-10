import os

import webapp2
import jinja2

from google.appengine.ext import db

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates/blog')),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True
)

class Post(db.Model):
    subject = db.StringProperty()
    content = db.TextProperty()
    created = db.DateTimeProperty(auto_now_add=True)


class MainPage(webapp2.RequestHandler):
    def get(self):
        context = {
            'posts': db.GqlQuery("SELECT * FROM Post")
        }

        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.out.write(template.render(context))


class NewPost(webapp2.RequestHandler):
    def get(self, subject="", content="", error=""):
        template = JINJA_ENVIRONMENT.get_template('new.html')
        context = {
            'subject': subject,
            'content': content,
            'error': error
        }
        self.response.out.write(template.render(context))

    def post(self):
        subject = self.request.get("subject")
        content = self.request.get("content")

        if subject and content:
            post = Post(subject=subject, content=content)

            post.put()

            self.redirect("/blog/%d" % post.key().id())
        else:
            error = "subject and content must both present"
            self.get(subject=subject, content=content, error=error)


class PostHandler(webapp2.RequestHandler):
    def get(self, id):
        post = Post.get_by_id(int(id))
        template = JINJA_ENVIRONMENT.get_template('post.html')
        context = {
            'post': post
        }
        self.response.out.write(template.render(context))

application = webapp2.WSGIApplication([
    (r'/blog', MainPage),
    (r'/blog/newpost', NewPost),
    (r'/blog/(\d+)', PostHandler),
], debug=True)
