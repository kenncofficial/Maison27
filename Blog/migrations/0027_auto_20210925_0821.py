# Generated by Django 3.1.2 on 2021-09-25 07:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0026_supply_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='categorys',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='general_supplies',
            old_name='supply_categorys',
            new_name='supply_category',
        ),
    ]