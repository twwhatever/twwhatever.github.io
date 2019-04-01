#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Ted'
SITENAME = "Ted Wild's Blog"
SITEURL = 'https://blog.tedwild.dev/'

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
LINKS = (('Résumé', 'https://blog.tedwild.dev/extras/tedwild.pdf'),
         ('My old page', 'http://pages.cs.wisc.edu/~wildt/'),)

# Social widget
SOCIAL = (('LinkedIn', 'https://www.linkedin.com/in/ted-wild'),
          ('GitHub', 'https://github.com/twwhatever'),)

DEFAULT_PAGINATION = False

STATIC_PATHS = ['extras']
EXTRA_PATH_METADATA = {'extras/CNAME': {'path': 'CNAME'},}

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
