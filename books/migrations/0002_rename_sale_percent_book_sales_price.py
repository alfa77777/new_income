# Generated by Django 4.2 on 2023-04-07 11:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='sale_percent',
            new_name='sales_price',
        ),
    ]