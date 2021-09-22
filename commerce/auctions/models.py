from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import related


class User(AbstractUser):
    pass

class Bids(models.Model):
    price = models.FloatField()


class Comments(models.Model):
    user = models.CharField(max_length=64)
    #user = models.ManyToManyField(User,blank=False,related_name="users")
    comment = models.TextField()


class Listings(models.Model):
    name = models.CharField(max_length=64)
    current_bid = models.ForeignKey(Bids, on_delete=models.CASCADE, related_name="bids")
    comments = models.ForeignKey(Comments, on_delete=models.CASCADE, related_name="comments")
    number_of_bids = models.IntegerField()

    def __str__(self):
        return f"{self.name} {self.price}"