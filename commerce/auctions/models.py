from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import related


class User(AbstractUser):
    pass

class Bid(models.Model):
    price = models.FloatField()
    number_of_bids = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.price}: {self.number_of_bids}"

class Comment(models.Model):
    user = models.CharField(max_length=64, default="user")
    #user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="users")
    comment = models.TextField()

    def __str__(self):
        return f"{self.user}: {self.comment}"


class Listing(models.Model):
    title = models.CharField(max_length=64)
    starting_bid = models.FloatField(default=0)
    bids = models.ManyToManyField(Bid, blank=True,related_name="bids")
    comments = models.ManyToManyField(Comment,blank=True, related_name="comments")
    description = models.TextField(default="description")

    def __str__(self):
        return f"{self.title} {self.starting_bid}"

