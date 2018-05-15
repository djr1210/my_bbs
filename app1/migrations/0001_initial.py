# Generated by Django 2.0.4 on 2018-05-15 08:17

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gtitle', models.CharField(max_length=20)),
                ('gtext', models.CharField(max_length=40)),
                ('gtime', models.DateTimeField(default=datetime.datetime(2018, 5, 15, 8, 17, 29, 427220))),
                ('gcount', models.IntegerField(default=0)),
                ('gisdelete', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Blogger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=10)),
                ('upassword', models.CharField(max_length=300)),
                ('uage', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='blog',
            name='gname',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.Blogger'),
        ),
    ]