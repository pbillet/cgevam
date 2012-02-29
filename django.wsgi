import os, sys  

sys.path.append('c:/Sites/')  
  
  
os.environ['DJANGO_SETTINGS_MODULE'] = 'cgevam.settings'  
  
  
import django.core.handlers.wsgi  
  
  
application = django.core.handlers.wsgi.WSGIHandler()  