import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'citygazette.settings')

application = get_wsgi_application()

# Выполним миграции и сбор статики автоматически при первом запуске
from django.core.management import call_command
call_command('migrate')
call_command('collectstatic', '--noinput')
