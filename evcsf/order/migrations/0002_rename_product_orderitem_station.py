# Generated by Django 4.2.2 on 2023-07-09 05:56

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("order", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="orderitem",
            old_name="product",
            new_name="station",
        ),
    ]
