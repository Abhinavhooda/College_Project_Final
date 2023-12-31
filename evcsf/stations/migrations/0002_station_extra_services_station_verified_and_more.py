# Generated by Django 4.2.2 on 2023-07-16 13:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("stations", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="station",
            name="Extra_Services",
            field=models.CharField(max_length=1500, null=True),
        ),
        migrations.AddField(
            model_name="station",
            name="Verified",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="station",
            name="owner_contact",
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AddField(
            model_name="station",
            name="owner_details",
            field=models.TextField(default=None, null=True),
        ),
        migrations.AddField(
            model_name="station",
            name="photos",
            field=models.ImageField(default=None, null=True, upload_to="uploads/"),
        ),
        migrations.AddField(
            model_name="station",
            name="video",
            field=models.FileField(
                default=None, null=True, upload_to="uploads/stations/videos"
            ),
        ),
    ]
