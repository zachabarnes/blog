#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Zach Barnes'
SITENAME = 'Blog'
SITESUBTITLE = ''
SITEURL = 'http://blog.zachabarnes.com'
GOOGLE_ANALYTICS = 'UA-replace-this'
DISQUS_SITENAME = 'replace-this'
AUTHOR_GITHUB = '@zachabarnes'
AUTHOR_TWITTER = 'replace-this'
AUTHOR_LINKEDIN = 'replace-this'
AUTHOR_EMAIL = 'me@zachabarnes.com'
AUTHOR_SLIDESHARE = 'replace-this'
SITE_DESCRIPTION = 'Blog'

PATH = 'content'
OUTPUT_PATH = 'output'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = u'en'
DEFAULT_DATE = 'fs'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
FEED_ALL_RSS = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

THEME = "Medio"

DIRECT_TEMPLATES = ('index', 'tags', 'categories', 'archives', 'blogroll')

BLOG_AUTHORS = {
    'Zach Barnes': {
        'description': """
            This is an example of description
        """,
        'short_description': """
            Data Analyst at John Doe LLC.
        """,
        'image': '../theme/images/authors/johndoe.png',
        'links': (('github', 'https://github.com/replace-this'),
                  ('twitter-square', 'https://twitter.com/replace-this')),
    }
}

BLOG_CATEGORIES = {
    'ggplot2': {
        'description': 'ggplot2 is a plotting system for R, based on the grammar of graphics, which tries to take the good parts of base and lattice graphics and none of the bad parts. It takes care of many of the fiddly details that make plotting a hassle (like drawing legends) as well as providing a powerful model of graphics that makes it easy to produce complex multi-layered graphics.',
        'thumbnail': '../theme/images/categories/ggplot2.png'
    }
}

MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb.markup']

# if you create jupyter files in the content dir, snapshots are saved with the same
# metadata. These need to be ignored. 
IGNORE_FILES = [".ipynb_checkpoints"] 