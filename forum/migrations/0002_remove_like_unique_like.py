# Generated by Django 3.2.10 on 2021-12-08 09:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='like',
            name='unique_like',
        ),
    ]
