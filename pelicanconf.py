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
LINKS = ()

# Social widget
SOCIAL = (('github', 'http://github.com/apatriz'),
          ('linkedin', 'http://linkedin.com/in/alecgis'),)
GITHUB_URL = 'http://github.com/apatriz'
LINKEDIN_URL = 'http://linkedin.com/in/alecgis'
TWITTER_URL = 'https://twitter.com/alecpatrizio'

# CUSTOM_CSS = 'static/extra_style.css'

STATIC_PATHS = ['images', 'extra/CNAME', ]
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
}

THEME = '/home/apatriz/Projects/apatriz.github.io/themes/pelican-bootstrap3'
BOOTSTRAP_THEME = 'alec'

BANNER = 'images/chameleon2.jpg'

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
