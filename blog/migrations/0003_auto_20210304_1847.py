# Generated by Django 3.1.7 on 2021-03-04 18:47

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('blog', '0002_auto_20210304_1846'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='image',
            new_name='image_url',
        ),
    ]
