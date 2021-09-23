from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.deletion import CASCADE, RESTRICT
from django.db.models.fields import related


class User(AbstractUser):
    pass


class Category(models.Model):
    category = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.category}"


class Listing(models.Model):

    title = models.CharField(max_length=64)
    image = models.URLField(max_length=500,blank=True)
    starting_bid = models.FloatField()
    number_of_bids = models.IntegerField(default=0)
    description = models.TextField(blank = False)
    category = models.ForeignKey(Category,on_delete=RESTRICT, related_name="categories")
    
    def __str__(self):
        return f"{self.title} {self.starting_bid}"

class Bid(models.Model):
    bid = models.FloatField(default=0)
    listing = models.ForeignKey(Listing,blank=False, on_delete=models.RESTRICT, related_name="bids")

    def __str__(self):
        return f"{self.price}: {self.number_of_bids}"

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.RESTRICT, related_name="users")
    comment = models.TextField()
    listing = models.ForeignKey(Listing, blank=False, on_delete=models.RESTRICT, related_name='comments')
    

    def __str__(self):
        return f"{self.user}: {self.comment}"