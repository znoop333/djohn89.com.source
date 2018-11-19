#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'djohn89'
SITENAME = 'djohn89.com'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'English'

THEME = '../pelican-blueidea'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

MENUITEMS = ( ('Presentations', 'presentations-list.html'), 
	      ('Publications (old)', '/science'),)

# Blogroll
LINKS = (('Publications (until 2013)', '/science'),
         ('Presentation List (since 2013)', 'presentations-list.html'),)

GOOGLE_ANALYTICS = 'UA-40728104-1'

DEFAULT_PAGINATION = 20

STATIC_PATHS = [
    'images',
    'css',
]

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
