# Generated by Django 3.2.7 on 2021-09-22 20:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bids',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=64)),
                ('comment', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Listings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('number_of_bids', models.IntegerField()),
                ('comments', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='auctions.comments')),
                ('current_bid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bids', to='auctions.bids')),
            ],
        ),
    ]