from google.appengine.ext import db

def page_key(group = 'default'):
    return db.Key.from_path('pages', group)


class Page(db.Model):
    slug = db.StringProperty(required = True)
    content = db.TextProperty()
    created_at = db.DateTimeProperty(auto_now_add=True)

    @classmethod
    def by_slug(cls, slug, version = None):
        pages = Page.all().filter('slug =', slug).order('-created_at')
        if version and version > 0 and version < pages.count():
            return list(pages)[-version]
        else:
            return pages.get()

    @classmethod
    def history_of(cls, slug):
        return Page.all().filter('slug =', slug).order('created_at')
