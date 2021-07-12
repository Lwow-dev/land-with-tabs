import os, sys
sys.path.append('/home/boss/www/django/land-dev')
os.environ['DJANGO_SETTINGS_MODULE'] = 'land-dev.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()