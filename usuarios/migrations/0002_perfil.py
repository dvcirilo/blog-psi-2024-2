# Generated by Django 5.1.2 on 2025-01-24 11:23

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cidade', models.CharField(max_length=100)),
                ('instagram', models.URLField(blank=True)),
                ('facebook', models.URLField(blank=True)),
                ('github', models.URLField(blank=True)),
                ('foto', models.ImageField(blank=True, upload_to='')),
                ('bio', models.TextField(blank=True, max_length=2000)),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
