# -*- coding: utf-8 -*-
AUTHOR = u'Michael Caron'
SITENAME = u"Mike's log"
SITEURL = 'http://mrcaron.github.com'

GITHUB_URL = 'http://github.com/mrcaron/'
DISQUS_SITENAME = "radhub"
PDF_GENERATOR = False
REVERSE_CATEGORY_ORDER = True
LOCALE = ""
DEFAULT_PAGINATION = 2

FEED_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'

LINKS = (('Code Rad', 'http://mrcaron.tumblr.com'),
        )

SOCIAL = (('twitter', 'http://twitter.com/radman'),
          ('lastfm', 'http://lastfm.com/user/mrcaron'),
          ('github', 'http://github.com/mrcaron'),)

# global metadata to all the contents
DEFAULT_METADATA = (('yeah', 'it is'),)

# static paths will be copied under the same name
STATIC_PATHS = ["pictures",]

# A list of files to copy from the source to the destination
FILES_TO_COPY = (('extra/robots.txt', 'robots.txt'),)

# foobar will not be used, because it's not in caps. All configuration keys
# have to be in caps
foobar = "barbaz"
