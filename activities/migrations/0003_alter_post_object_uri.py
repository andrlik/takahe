# Generated by Django 4.1.3 on 2022-11-13 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("activities", "0002_fan_out"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="object_uri",
            field=models.CharField(blank=True, max_length=500, null=True, unique=True),
        ),
    ]