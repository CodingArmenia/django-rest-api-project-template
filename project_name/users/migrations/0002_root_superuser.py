from decouple import config
from django.db import migrations


def forwards_create_superuser(apps, schema_editor):
    user = apps.get_model('users', 'User')
    user.objects.create_superuser(
        username=config('ROOT_SUPERUSER_USERNAME', default='admin'),
        email=config('ROOT_SUPERUSER_EMAIL', default='admin@gmail.com'),
        password=config('ROOT_SUPERUSER_PASSWORD', default='admin123'),
        first_name=config('ROOT_SUPERUSER_FIRST_NAM', default='Admin'),
        last_name=config('ROOT_SUPERUSER_LAST_NAME', default='Admin')
    )


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(forwards_create_superuser)
    ]
