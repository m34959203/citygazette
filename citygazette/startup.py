# citygazette/startup.py

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'citygazette.settings')

# Выполняем collectstatic при запуске (для Render)
try:
    from django.core.management import call_command
    call_command('collectstatic', '--noinput')
except Exception as e:
    print(f"❗ Ошибка при выполнении collectstatic: {e}")

application = get_wsgi_application()
