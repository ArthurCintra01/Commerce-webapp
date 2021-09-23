# Generated by Django 3.2.7 on 2021-09-23 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0014_auto_20210923_1638'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='listing',
            field=models.ManyToManyField(blank=True, related_name='categories', to='auctions.Listing'),
        ),
        migrations.RemoveField(
            model_name='category',
            name='category',
        ),
        migrations.AddField(
            model_name='category',
            name='category',
            field=models.CharField(blank=True, max_length=64),
        ),
    ]
