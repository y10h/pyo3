#!/usr/bin/env python
"""
Migration script for move data from Byteflow instance and generate Cyrax site
"""

import os
import re
import string
from cyraxlib import utils

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
import settings
import blog.models
from django.contrib.flatpages import models as flatpages



POST_TEMPLATE = string.Template(u"""\
{% meta %}
    tags: [$tags]
    title: $title
{% endmeta %}

{% mark body %}$filter
$post
$endfilter{% endmark %}
""")

PAGE_TEMPLATE = string.Template(u"""\
{% meta %}
    title: $title
{% endmeta %}

{% block content %}
$content
{% endblock %}
""")


PATH_TEMPLATE = string.Template('$year/$month-$day-$slug.$format')


def get_post_context(bf_post):
    """
    Dump post (meta)data to simple dict
    """
    data = {
        'title': bf_post.name,
        'slug': bf_post.slug,
        'post': jinja_escape(bf_post.text),
        'timestamp': str(bf_post.date),
        'year': '%d' % bf_post.date.year,
        'month': '%02d' % bf_post.date.month,
        'day': '%02d' % bf_post.date.day,
        'format': bf_post.render_method,
        'tags': bf_post.tags,
    }
    if data['format'] == 'html':
        data['filter'] = ''
        data['endfilter'] = ''
    elif data['format'] == 'markdown':
        data['filter'] = '{% filter markdown %}'
        data['endfilter'] = '{% endfilter %}'
    else:
        raise ValueError(
            "Format %(format)s is not supported yet (inside post %(slug)s)"
            % data
        )
    return data


def jinja_escape(text):
    for statement, repl in (
        (r"{{(.+?)}}", r"{{ '{{' }}\1{{ '}}' }}"),
        (r"{%(.+?)%}", r"{{ '{%' }}\1{{ '%}' }}"),
    ):
        text = re.sub(statement, repl, text)
    return text

def write_cyrax(template, context, path):
    dirname = os.path.dirname(path)
    if not os.path.exists(dirname):
        os.makedirs(dirname)
    fh = open(path, 'w')
    fh.write(template.substitute(context).encode('utf-8'))
    fh.close()


def get_cyrax_path(target, template, context):
    relative = template.substitute(context)
    return os.path.join(target, relative)

    
def dump_blog_posts(target, post_template=POST_TEMPLATE,
                    path_template=PATH_TEMPLATE):
    for post in blog.models.Post.objects.all():
        context = get_post_context(post)
        path = get_cyrax_path(target, path_template, context)
        write_cyrax(post_template, context, path)
        print "Post: %s -> %s" % (post.slug, path)



def get_page_context(page, target):
    context = dict(
        (k, getattr(page, k))
        for k in ('title', 'content')
    )
    url = page.url
    if url.startswith('/'):
        url = url[1:]
    context['url'] = url
    path = utils.url2path(context['url'])
    if path.endswith(os.path.sep):
        path += 'index.html'
    else:
        path += '.html'
    context['path'] = os.path.join(target, path)
    return context


def dump_flat_pages(target, page_template=PAGE_TEMPLATE):
    for page in flatpages.FlatPage.objects.all():
        context = get_page_context(page, target)
        write_cyrax(page_template, context, context['path'])
        print "Page: %(url)s -> %(path)s" % context

def dump_all(target):
    dump_flat_pages(target)
    dump_blog_posts(target)

if __name__ == '__main__':
    import sys
    dump_all(sys.argv[1])

