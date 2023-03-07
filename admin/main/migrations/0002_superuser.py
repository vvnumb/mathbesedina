from __future__ import unicode_literals

from django.db import migrations
from main.models import CustomUser as User


def create_superuser(apps, schema_editor):
    superuser = User()
    superuser.is_active = True
    superuser.is_superuser = True
    superuser.is_staff = True
    superuser.username = 'admin'
    superuser.email = 'admin@admin.net'
    superuser.set_password('admin')
    superuser.save()


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_superuser)
    ]