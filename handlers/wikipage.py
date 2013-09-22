from mainhandler import MainHandler
from models.pages import Page

class WikiPage(MainHandler):
    def get(self, page_slug):
        page = Page.by_slug(page_slug)
        if page:
            self.render("page.html", page = page)
        else:
            self.redirect("/_edit%s" % page_slug)