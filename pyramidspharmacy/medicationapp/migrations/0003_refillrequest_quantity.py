# Generated by Django 4.2.16 on 2024-11-06 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicationapp', '0002_refillrequest_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='refillrequest',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]
