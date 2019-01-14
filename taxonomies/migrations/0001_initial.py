# Generated by Django 2.1.5 on 2019-01-14 17:05

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('meta', django.contrib.postgres.fields.jsonb.JSONField(default=dict)),
                ('slug', models.SlugField(max_length=128)),
                ('title', models.TextField(max_length=512)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
