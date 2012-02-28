import os, sys  
  
  
sys.path.append('c:/wamp/www/')  
  
  
os.environ['DJANGO_SETTINGS_MODULE'] = 'cgevam.settings'  
  
  
import django.core.handlers.wsgi  
  
  
application = django.core.handlers.wsgi.WSGIHandler()  