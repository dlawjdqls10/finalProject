# Generated by Django 2.1.5 on 2019-06-10 11:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_profile_profile_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='profile_pic',
        ),
    ]
