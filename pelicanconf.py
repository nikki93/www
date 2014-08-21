#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

EMAIL = u's.nikhilesh@gmail.com'
GITHUB = u'https://github.com/nikki93'
AUTHOR = u'Nikhilesh Sigatapu'
SITENAME = u'nikhilesh.info'
SITEURL = 'http://localhost:8000'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

STATIC_PATHS = ['images', 'files']
#THEME = '../pelican-themes/simple-bootstrap'
THEME = 'themes/just-read'

DISPLAY_CATEGORIES_ON_SUBMENU = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  ()

# Social widget
SOCIAL = ()

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
