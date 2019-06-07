# Generated by Django 2.1.5 on 2019-06-07 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidates2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('item_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('brand', models.CharField(max_length=50, null=True)),
                ('image', models.TextField(null=True)),
                ('texts', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Prediction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prediction', models.FloatField(null=True)),
                ('user_id', models.IntegerField(null=True)),
                ('item_id', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(default='just testing content for rate model, confliction with views.save_rate')),
                ('review', models.TextField(null=True)),
                ('rate', models.IntegerField()),
                ('item_id', models.IntegerField()),
                ('user_id', models.IntegerField()),
                ('created_at', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.IntegerField(primary_key=True, serialize=False)),
                ('gender', models.CharField(default='F', max_length=10)),
                ('skin_type', models.CharField(max_length=10)),
                ('age', models.FloatField(null=True)),
                ('nickname', models.CharField(default='anonymous', max_length=20)),
                ('profile', models.TextField(null=True)),
                ('candidates', models.ManyToManyField(blank=True, to='catalog.User')),
            ],
        ),
        migrations.AddField(
            model_name='candidates2',
            name='user_from',
            field=models.ManyToManyField(related_name='user_from', to='catalog.User'),
        ),
        migrations.AddField(
            model_name='candidates2',
            name='user_to',
            field=models.ManyToManyField(related_name='user_to', to='catalog.User'),
        ),
    ]
