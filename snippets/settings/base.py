# This is your project's main settings file that can be committed to your
# repo. If you need to override a setting locally, use settings_local.py

from funfactory.settings_base import *  # NOQA


# Defines the views served for root URLs.
ROOT_URLCONF = 'snippets.urls'

INSTALLED_APPS = list(INSTALLED_APPS) + [
    'snippets.base',

    # Django contrib apps
    'django.contrib.admin',

    # Libraries
    'django_ace',
    'django_filters',
    'smuggler',
    'south',
    'waffle',
]

# Because Jinja2 is the default template loader, add any non-Jinja templated
# apps here:
JINGO_EXCLUDE_APPS = [
    'admin',
    'smuggler',
    'registration',
]

# Should robots.txt deny everything or disallow a calculated list of URLs we
# don't want to be crawled?  Default is false, disallow everything.
# Also see http://www.google.com/support/webmasters/bin/answer.py?answer=93710
ENGAGE_ROBOTS = False

# Always generate a CSRF token for anonymous users.
ANON_ALWAYS = True

# Caching
CACHE_EMPTY_QUERYSETS = True

LOGGING = {
    'loggers': {
        'playdoh': {
            'level': logging.DEBUG
        },
        'south': {
            'level': logging.ERROR
        }
    }
}

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    'session_csrf.context_processor',
    'django.contrib.messages.context_processors.messages',
    'funfactory.context_processors.globals',
)

MIDDLEWARE_CLASSES = (
    'snippets.base.middleware.FetchSnippetsMiddleware',
    'multidb.middleware.PinningRouterMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'session_csrf.CsrfMiddleware',  # Must be after auth middleware.
    'django.contrib.messages.middleware.MessageMiddleware',
    'commonware.middleware.FrameOptionsHeader',
)

DATABASE_ROUTERS = ()


# Set ALLOWED_HOSTS based on SITE_URL.
def _allowed_hosts():
    from django.conf import settings
    from urlparse import urlparse

    host = urlparse(settings.SITE_URL).netloc  # Remove protocol and path
    host = host.rsplit(':', 1)[0]  # Remove port
    return [host]
ALLOWED_HOSTS = lazy(_allowed_hosts, list)()

# CDN_URL = 'https://snippets.cdn.mozilla.net/'

SNIPPET_SIZE_LIMIT = 500
SNIPPET_IMAGE_SIZE_LIMIT = 250

SOUTH_MIGRATION_MODULES = {
    'waffle': 'waffle.south_migrations',
}

SNIPPET_BUNDLE_TIMEOUT = 15 * 60  # 15 minutes

METRICS_URL = 'https://snippets-stats.mozilla.org/foo.html'
METRICS_SAMPLE_RATE = 0.1

GEO_URL = 'https://location.services.mozilla.com/v1/country?key=fff72d56-b040-4205-9a11-82feda9d83a3'
