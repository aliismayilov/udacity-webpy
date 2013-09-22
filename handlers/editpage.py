from mainhandler import MainHandler, wiki_key
from models.pages import Page
import time
import logging

class EditPage(MainHandler):
    def get(self, page_slug):
        if self.user:
            page = Page.by_slug(page_slug)
            self.render("edit_page.html", page = page)
        else:
            self.redirect('/login')
    def post(self, page_slug):
        if self.user:
            content = self.request.get('content', '')

            if content:
                page = Page(parent = wiki_key(), slug = page_slug, content = content)
                page.put()
                time.sleep(0.1)
                self.redirect(page.slug)
            else:
                error = "content, please!"
                self.render("edit_page.html", page=Page(parent = wiki_key(), slug = page_slug, content = content), error=error)
        else:
            self.redirect('/login')
