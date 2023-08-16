# Generated by Django 3.2.19 on 2023-06-17 22:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Serial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_number', models.CharField(max_length=100, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('creator', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='serials_created', to=settings.AUTH_USER_MODEL)),
                ('editor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='serials_edited', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
