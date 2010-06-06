"""
Extensions for Cyrax (http://pypi.python.org/pypi/cyrax) for pyobject.ru v3
"""

from cyraxlib import core, events, models,  utils

class PostPermalink(object):
    """
    Links from /blog/post/<slug>/ to /blog/<YYYY>/<MM>/<DD>/<slug>/
    """

    prefix = 'blog/post/'

    @classmethod
    def check(cls, entry):
        res = entry.path.startswith(utils.url2path(self.prefix))
        return res

    def __init__(self):
        self.slug = self.path[len(self.prefix):-len('.html')]

    def __str__(self):
        return self.slug

    def get_relative_url(self):
        if self.path.endswith('.html'):
            url = utils.path2url(self.path[:-len('.html')])
        else:
            url = utils.path2url(self.path)
        if self.isdir():
            url += '/'
        return url



def add_posts_permalinks(site):
    site.permalinks = {}
    for post in site.posts:
        path = '%s%s.html' % (PostPermalink.prefix, post.slug)
        site.entries.append(core.Entry(site, path, '_permalink.html'))
        site.permalinks[post.slug] = post.get_absolute_url()

def callback(site):
    events.events.connect('site-traversed', add_posts_permalinks)
    models.TYPE_LIST.append(PostPermalink)

