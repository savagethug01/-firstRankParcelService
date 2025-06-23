#!/bin/sh

set -e  # Exit on error

echo "🔄 Running makemigrations..."
python manage.py makemigrations --noinput
echo "✅ Makemigrations completed!"

echo "🔄 Running database migrations..."
python manage.py migrate --noinput
echo "✅ Migrations applied!"

echo "👤 Deleting old superuser (if exists) and creating new one..."

python manage.py shell << END
from django.contrib.auth import get_user_model

User = get_user_model()
username = "admin"
email = "adminmail@gmail.com"
password = "adminpass"

user = User.objects.filter(username=username).first()
if user:
    user.delete()
    print(f"🗑️ Existing superuser '{username}' deleted.")
User.objects.create_superuser(username=username, email=email, password=password)
print(f"✅ New superuser '{username}' created successfully.")
END

echo "🚀 Starting Django development server..."
exec python manage.py runserver 0.0.0.0:8000
