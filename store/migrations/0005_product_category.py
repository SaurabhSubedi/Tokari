# Generated by Django 4.1.1 on 2023-06-21 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_product_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(blank=True, choices=[('Clothes', 'Clothes'), ('Electronics', 'Electronics'), ('Jerseys', 'Jerseys')], max_length=20, null=True),
        ),
    ]