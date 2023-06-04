# Generated by Django 4.2.1 on 2023-06-04 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0030_delete_label_product_label'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='label',
            field=models.CharField(choices=[('NEW', 'primary'), ('BEST', 'success'), ('SALE', 'danger')], default='NEW', max_length=150),
        ),
    ]
