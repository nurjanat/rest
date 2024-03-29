# Generated by Django 3.1.7 on 2021-03-10 09:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rests', '0007_auto_20210309_1106'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='contact',
            name='branch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to='rests.branch'),
        ),
    ]
