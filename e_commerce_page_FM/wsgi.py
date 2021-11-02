import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'e_commerce_page_FM.settings')

application = get_wsgi_application()
