# Generated by Django 3.0.3 on 2020-03-13 17:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GymWebapp', '0004_auto_20200313_2207'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscription',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='subscription',
            name='package',
        ),
    ]
