# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name=b'Type',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                (b'problem_type', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name=b'Ticket',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                (b'title', models.CharField(max_length=30)),
                (b'content', models.TextField()),
                (b'priority', models.IntegerField(default=0, choices=[(0, b'Low'), (1, b'Normal'), (2, b'High')])),
                (b'status', models.IntegerField(default=0)),
                (b'queue', models.ForeignKey(to=b'ticket_engine.Type', to_field='id')),
                (b'user', models.CharField(max_length=8)),
                (b'pub_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'date published')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
