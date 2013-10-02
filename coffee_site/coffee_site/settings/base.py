# Django settings for coffee_site project.

from unipath import Path

PROJECT_ROOT = Path(__file__).ancestor(3)

# Absolute filesystem path to the directory that will hold user-uploaded files.
MEDIA_ROOT = PROJECT_ROOT.child("media")

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
STATIC_ROOT = ""
STATIC_URL = "/static/" ## PROJECT_ROOT.child("static")

# Additional locations of static files
STATICFILES_DIRS = (
    PROJECT_ROOT.child("static"),
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

TEMPLATE_DIRS = (
    PROJECT_ROOT.child("templates"),
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

FIXTURE_DIRS = (
    PROJECT_ROOT.child("fixtures"),
    PROJECT_ROOT.child("general").child("fixtures"),
    PROJECT_ROOT.child("coffee_bag").child("fixtures"),
)

ADMINS = (
    ('Kenneth Daily', 'kmdaily@gmail.com'),
    ('Vesna Memisevic', 'vesna.memisevic@gmail.com'),
)

MANAGERS = ADMINS

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
#         'NAME': 'djangocoffee',     # Or path to database file if using sqlite3.
#         'USER': 'dailykm',                      # Not used with sqlite3.
#         'PASSWORD': '2Sr3x99g',                  # Not used with sqlite3.
#         'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
#         'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
#     }
# }

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/New_York'

# DISQUS configuration
# Needs to be changed - I created an account - vessykenny
DISQUS_API_KEY = 'FOOBARFOOBARFOOBARFOOBARFOOBARF'
DISQUS_WEBSITE_SHORTNAME = 'foobar'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'


#Easy map setup
EASY_MAPS_CENTER = (-41.3, 32)


SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True


# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = "http://localhost:8000/media/"


# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'suy155wk$vkaz-p0z+e24*k#ckw7nt-aiy0489-x9qh9b#xc*^'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'coffee_site.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'coffee_site.wsgi.application'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',

    # our apps
    'general',
    'profile',
    'coffee_bag',
    'coffee_ratio',

    ## External apps
    'disqus',
    'guardian',
    'localflavor',
    'django_countries',
    'easy_maps',
    
    # # Not compatible with Django 1.5 (doesn't work with custom user class)
    # # Pull request in github repo has been made to add this functionality,
    # # but has not been merged (see https://github.com/kdaily/coffee/issues/10)
    'djangoratings',

    'sorl.thumbnail',
    'braces',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,

    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
            },
        'simple': {
            'format': '%(levelname)s %(message)s'
            },
        },
    
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
            }
        },
    
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
            },
        'console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler',
            'formatter': 'simple'
            },   
        },

    'loggers': {
        'django': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'INFO',
            },
        'views': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'DEBUG',
            },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
            },
        }
    }


# For django-guardian
ANONYMOUS_USER_ID = -1

# Use a new user model
AUTH_USER_MODEL = "profile.CoffeeUser"


# URL of the login page.
# LOGIN_URL = '/login/'
