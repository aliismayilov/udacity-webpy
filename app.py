import webapp2
import models
import handlers
from handlers.signup import Signup
from handlers.login import Login
from handlers.logout import Logout
from handlers.wikipage import WikiPage
from handlers.editpage import EditPage
from settings import DEBUG

PAGE_RE = r'(/(?:[a-zA-Z0-9_-]+/?)*)'
app = webapp2.WSGIApplication([('/signup', Signup),
                               ('/login', Login),
                               ('/logout', Logout),
                               ('/_edit' + PAGE_RE, EditPage),
                               (PAGE_RE, WikiPage),
                               ],
                              debug=DEBUG)