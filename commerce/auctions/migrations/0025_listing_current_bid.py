# Generated by Django 3.2.7 on 2021-09-24 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0024_alter_listing_starting_bid'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='current_bid',
            field=models.FloatField(default=0),
        ),
    ]
