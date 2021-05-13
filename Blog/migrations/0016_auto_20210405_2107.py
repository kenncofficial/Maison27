# Generated by Django 3.1.2 on 2021-04-05 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0015_blogpost_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='tags',
        ),
        migrations.AddField(
            model_name='blogpost',
            name='blog_quote',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
