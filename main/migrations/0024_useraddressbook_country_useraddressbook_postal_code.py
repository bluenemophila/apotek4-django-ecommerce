# Generated by Django 4.2.1 on 2023-06-03 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_cartorder_coupon'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraddressbook',
            name='country',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='useraddressbook',
            name='postal_code',
            field=models.CharField(max_length=15, null=True),
        ),
    ]