#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
<<<<<<< HEAD:backend/manage.py
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
=======
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
>>>>>>> 445d0d904105fda7c3ae6eebdb32bb0c1c2924b5:manage.py
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
