# Generated by Django 3.0.2 on 2020-01-23 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matrix', '0002_auto_20200123_0952'),
    ]

    operations = [
        migrations.CreateModel(
            name='local_bodies_id',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]
