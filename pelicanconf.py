#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Alec Patrizio'
SITENAME = 'Alec Patrizio'
SITEURL = 'http://alecpatrizio.com'

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

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
SOCIAL = (('Github', 'http://github.com/apatriz'),
          ('Linkedin', 'http://linkedin.com/in/alecgis'),)
GITHUB_URL = 'http://github.com/apatriz'
LINKEDIN_URL = 'http://linkedin.com/in/alecgis'
TWITTER_URL = 'https://twitter.com/alecpatrizio'

# CUSTOM_CSS = 'static/extra_style.css'

STATIC_PATHS = ['images', 'extra/CNAME', 'extra/favicon.ico', 'extra/logo.svg']
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/logo.svg': {'path': 'logo.svg'}
}

THEME = 'nest'
### Template settings ###

## Theme: pelican-bootstrap3
# BOOTSTRAP_THEME = 'alec'
# BANNER = 'images/chameleon2.jpg'

## Theme: Nest Settings
NEST_HEADER_IMAGES = ''
SITESUBTITLE = u"Only This Moment"
# index.html
NEST_INDEX_HEAD_TITLE = u'Alec Patrizio'
NEST_INDEX_HEADER_TITLE = u"There's Only This Moment"
NEST_INDEX_HEADER_SUBTITLE = u'Oodalalee, oodalalee, golly what a day'
NEST_INDEX_CONTENT_TITLE = u'Last Posts'
# Footer
NEST_SITEMAP_COLUMN_TITLE = u'Sitemap'
NEST_SITEMAP_MENU = [('Archives', '/archives.html'),('Tags','/tags.html'), ('Authors','/authors.html')]
NEST_SITEMAP_ATOM_LINK = u'Atom Feed'
# NEST_SITEMAP_RSS_LINK = u'RSS Feed'
NEST_SOCIAL_COLUMN_TITLE = u'Social'
# NEST_LINKS_COLUMN_TITLE = u'Links'
NEST_COPYRIGHT = u'&copy; Alec Patrizio 2016'




DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
