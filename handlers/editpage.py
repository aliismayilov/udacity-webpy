from mainhandler import MainHandler, wiki_key
from models.pages import Page

class EditPage(MainHandler):
    def get(self, page_slug):
        if self.user:
            page = Page.by_slug(page_slug)
            self.render("edit_page.html", page = page)
        else:
            self.redirect('/login')
    def post(self, page_slug):
        if self.user:
            content = self.request.get('content').strip()

            if content and content != '':
                page = Page.by_slug(page_slug)
                if not page:
                    page = Page(parent = wiki_key(), slug = page_slug)
                page.content = content
                page.put()
                self.redirect(page.slug)
            else:
                error = "content, please!"
                self.render("edit_page.html", content=content, error=error)
        else:
            self.redirect('/login')
