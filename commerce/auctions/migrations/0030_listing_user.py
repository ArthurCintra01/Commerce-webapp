# Generated by Django 3.2.7 on 2021-09-24 19:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0029_alter_bid_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.RESTRICT, related_name='listing_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
