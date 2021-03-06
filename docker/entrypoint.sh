#!/bin/bash
set -e
cd /site

pip install service_identity

if [ -f /kindlegen/kindlegen ]; then
  mv /kindlegen/kindlegen /site/kmanga/bin
fi

echo "BEFORE MIGRATIONS"
#export PYTHONPATH=/site:/site/kmanga:/site/scraper


kmanga/manage.py makemigrations

cp bin/0002_full_text_search.py kmanga/core/migrations/
kmanga/manage.py migrate
echo "from django.contrib.auth.models import User; User.objects.create_superuser('kmanga', 'luis.caldeira@gmail.com', 'kmanga')" | kmanga/manage.py shell
#kmanga/manage.py createsuperuser --username kmanga --noinput --email luis.caldeira@gmail.com
kmanga/manage.py loaddata bin/initialdata.json


echo "AFTER MIGRATIONS"
exec "$@"
