# Generated by Django 3.1.7 on 2021-03-05 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rests', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('pending', 'pending'), ('finished', 'finished')], default='pending', max_length=20),
        ),
    ]
