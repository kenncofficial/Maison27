# Generated by Django 3.1.2 on 2021-02-21 21:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0009_auto_20210221_2148'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='date_posted',
            new_name='post_date',
        ),
    ]
