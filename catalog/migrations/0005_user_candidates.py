# Generated by Django 2.1.7 on 2019-06-03 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_auto_20190530_2212'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='candidates',
            field=models.ManyToManyField(blank=True, to='catalog.User'),
        ),
    ]
