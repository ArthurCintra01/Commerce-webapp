# Generated by Django 3.2.7 on 2021-09-26 05:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0034_listing_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='winner',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.RESTRICT, related_name='winner', to=settings.AUTH_USER_MODEL),
        ),
    ]
