# Generated by Django 2.1.5 on 2019-01-14 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmarks', '0002_auto_20190114_1859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmark',
            name='tags',
            field=models.ManyToManyField(blank=True, to='taxonomies.Tag'),
        ),
    ]
