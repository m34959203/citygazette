# citygazette/startup.py

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'citygazette.settings')

try:
    # Убедимся, что папка для статики существует
    os.makedirs(os.path.join(os.path.dirname(__file__), '..', 'staticfiles'), exist_ok=True)

    # Собираем статику
    from django.core.management import call_command
    call_command('collectstatic', interactive=False, verbosity=0)
    print("✅ collectstatic успешно выполнен")
except Exception as e:
    print(f"❗ Ошибка при collectstatic: {e}")

application = get_wsgi_application()
