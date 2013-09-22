from google.appengine.ext import db

def page_key(group = 'default'):
    return db.Key.from_path('pages', group)


class Page(db.Model):
    slug = db.StringProperty(required = True)
    content = db.TextProperty()

    @classmethod
    def by_id(cls, uid):
        return Page.get_by_id(uid, parent = page_key())

    @classmethod
    def by_slug(cls, slug):
        p = Page.all().filter('slug =', slug).get()
        return p
