# Generated by Django 3.2.7 on 2021-09-23 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0011_listing_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='image',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
