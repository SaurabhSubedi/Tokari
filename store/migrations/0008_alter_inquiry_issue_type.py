# Generated by Django 4.1.1 on 2023-06-27 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_inquiry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inquiry',
            name='issue_type',
            field=models.CharField(max_length=50),
        ),
    ]