# Generated by Django 3.2.7 on 2021-09-22 20:57

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_auto_20210922_1748'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='current_bid',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='number_of_bids',
        ),
        migrations.AddField(
            model_name='bid',
            name='number_of_bids',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='listing',
            name='bids',
            field=models.ManyToManyField(blank=True, related_name='bids', to='auctions.Bid'),
        ),
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ManyToManyField(related_name='users', to=settings.AUTH_USER_MODEL),
        ),
    ]
