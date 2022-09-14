release: sh -c 'python manage.py migrate && python manage.py loaddata initial_catalog_data.json'
web: gunicorn tugas2pbp-falensiazmi.wsgi --log-file -