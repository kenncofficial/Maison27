# Generated by Django 3.1.2 on 2021-02-18 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0006_auto_20210218_1620'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='header_image',
            new_name='blog_image',
        ),
    ]