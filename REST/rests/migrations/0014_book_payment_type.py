# Generated by Django 3.1.7 on 2021-03-17 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rests', '0013_book_sale_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='payment_type',
            field=models.CharField(choices=[('card', 'card'), ('cash', 'cash')], default='cash', max_length=90),
        ),
    ]
