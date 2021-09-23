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
    user = models.ForeignKey(User, on_delete=models.RESTRICT, related_name="users")
    comment = models.TextField()

    def __str__(self):
        return f"{self.user}: {self.comment}"

class Category(models.Model):
    category = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.category}"


class Listing(models.Model):

    title = models.CharField(max_length=64)
    image = models.URLField(max_length=500,blank=True)
    starting_bid = models.FloatField()
    bids = models.ManyToManyField(Bid, blank= True, related_name="bids")
    comments = models.ManyToManyField(Comment,blank= True, related_name="comments")
    description = models.TextField(blank = False)
    category = models.ManyToManyField(Category, blank= True, related_name="categories")
    
    def __str__(self):
        return f"{self.title} {self.starting_bid}"

