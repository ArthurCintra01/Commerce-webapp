# Generated by Django 3.2.7 on 2021-09-24 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0023_alter_comment_listing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='starting_bid',
            field=models.FloatField(default=0),
        ),
    ]
