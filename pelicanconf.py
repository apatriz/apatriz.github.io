#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Alec Patrizio'
SITENAME = 'Alec Patrizio'
SITEURL = 'http://blog.alecpatrizio.com'

PATH = 'content'

TIMEZONE = 'America/Detroit'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

STATIC_PATHS = ['images', 'extra/CNAME', ]
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}, }

THEME = '/home/apatriz/Projects/pelican-themes/pelican-bootstrap3'
BOOTSTRAP_THEME = 'sandstone'

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
