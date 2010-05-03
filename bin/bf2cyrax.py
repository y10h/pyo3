#!/usr/bin/env python
"""
Migration script for move data from Byteflow instance and generate Cyrax site
"""

import os
import string

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
import settings
import blog.models



POST_TEMPLATE = string.Template(u"""\
{% meta %}
    tags: [$tags]
    title: $title
{% endmeta %}

{% mark body %}$filter
$post
$endfilter{% endmark %}
""")


PATH_TEMPLATE = string.Template('$year/$month-$day-$slug.$format')


def get_post_context(bf_post):
    """
    Dump post (meta)data to simple dict
    """
    data = {
        'title': bf_post.name,
        'slug': bf_post.slug,
        'post': bf_post.text,
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


def write_cyrax_post(template, context, path):
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
        write_cyrax_post(post_template, context, path)
        print "%s -> %s" % (post.slug, path)


if __name__ == '__main__':
    import sys
    dump_blog_posts(sys.argv[1])

