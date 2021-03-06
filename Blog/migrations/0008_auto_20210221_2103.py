# Generated by Django 3.1.2 on 2021-02-21 20:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0007_auto_20210218_1625'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='body',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='post_date',
            new_name='date_posted',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='blog_image',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='title_tag',
            new_name='subtitle',
        ),
    ]
