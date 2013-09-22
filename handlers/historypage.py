from mainhandler import MainHandler
from models.pages import Page

class HistoryPage(MainHandler):
    def get(self, page_slug):
        pages = Page.history_of(page_slug)
        self.render("history.html", pages = pages)