AUTHOR = 'forkliu'
SITENAME = 'FORKLIU'
SITEURL = "https://forkliu.com"
ORGNIZATION = "FORKLIU"
PATH = "content"

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = 'en'

AUTHORS = {
  'forkliu': {
    'avatar': '/images/avatars/tiger.png',
    'bio': "Graduated in Computer Science and Engineering, but currently working with GNU/Linux infrastructure and in the spare time I'm an Open Source programmer (Python and C), a drawer and author in the FORKLIU Blog.",
    'links': [
        ("GitHub", "github", "#"),
        ("Twitter", "twitter", "#"),
        ("Google Plus", "google-plus", "#"),
        ("Facebook", "facebook", "#"),
    ]
  }
}

ARTICLE_URL = 'categories/{category}/{slug}'
ARTICLE_SAVE_AS = 'categories/{category}/{slug}/index.html'

PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}/index.html'

AUTHORS_URL = "authors"
AUTHOR_URL = 'authors/{slug}'
AUTHOR_SAVE_AS = 'authors/{slug}/index.html'

CATEGORIES_URL = "categories"
CATEGORY_URL = 'categories/{slug}'
CATEGORY_SAVE_AS = 'categories/{slug}/index.html'

TAGS_URL = "tags"
TAG_URL = 'tags/{slug}'
TAG_SAVE_AS = 'tags/{slug}/index.html'

DEFAULT_PAGINATION = 10

I18N_TEMPLATES_LANG = 'en'

THEME = "themes/papyrus"
JINJA_ENVIRONMENT = {
  'extensions': [ 'jinja2.ext.do']
}

SHOW_DATE_MODIFIED = True
SHOW_ARTICLE_AUTHOR = True
SHOW_ARTICLE_CATEGORY = True

FAVICON = "extra/favicon-32x32.png"
TOUCHICON = "extra/apple-touch-icon.png"


FEED_ALL_ATOM = "feeds.atom"
FEED_ALL_RSS = "feeds.rss"

GOOGLE_ANALYTICS = "G-SBY82C4X3X"

TAG_CLOUD_STEPS = 4
TAG_CLOUD_BADGE = True
TAG_CLOUD_MAX_ITEMS=25

MD_INCLUDE_BASE_PATH = "sourcecode"

STATIC_PATHS = [
    'images',
    'extra',  # this
]

EXTRA_PATH_METADATA = {
    'extra/favicon.png': {'path': 'favicon.png'},  # and this
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/CNAME': {'path': 'CNAME'},
    'extra/app-ads.txt': {'path': 'app-ads.txt'},
}

GISGUS_REPO_NAME = "vforkliu/vforkliu.github.io"
GISGUS_REPO_ID = "MDEwOlJlcG9zaXRvcnkxOTMwNTY0Mjc="
GISGUS_CATEGORY_NAME = "Announcements"
GISGUS_CATEGORY_ID = "DIC_kwDOC4HOq84CxFIs"

SUBTITLE = "FORKLIU's BLOG"
SUBTEXT = "I'm a drawer and author in the FORKLIU Blog."
COPYRIGHT = "© 2025 FORKLIU. All rights reserved."