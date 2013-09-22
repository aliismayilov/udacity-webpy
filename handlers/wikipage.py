from mainhandler import MainHandler
from models.pages import Page


class WikiPage(MainHandler):
    def get(self, page_slug):
        version = self.request.get('v')
        if version.isdigit():
            version = int(version)
        else:
            version = None

        page = Page.by_slug(page_slug, version = version)
        if page:
            self.render("page.html", page = page)
        else:
            self.redirect("/_edit%s" % page_slug)
