# Generated by Django 3.0.3 on 2020-03-13 17:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GymWebapp', '0005_auto_20200313_2252'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='customer',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='GymWebapp.Customer_Details'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subscription',
            name='package',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='GymWebapp.Packages'),
            preserve_default=False,
        ),
    ]