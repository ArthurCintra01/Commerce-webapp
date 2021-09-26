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
    watchlist = models.ManyToManyField(User,blank=True, related_name="watchlist_users")
    user = models.ForeignKey(User,default=None, on_delete=models.RESTRICT, related_name="listing_user")
    title = models.CharField(max_length=64)
    image = models.URLField(max_length=500,blank=True)
    starting_bid = models.FloatField(default=0)
    current_bid = models.FloatField(default=0)
    number_of_bids = models.IntegerField(default=0)
    description = models.TextField(blank = False)
    category = models.ForeignKey(Category,on_delete=RESTRICT, blank=True, related_name="listings_category")
    is_active = models.BooleanField(default=True)
    winner = models.ForeignKey(User,default=None, blank=True, on_delete=models.RESTRICT, related_name="winner")
    
    def __str__(self):
        return f"{self.title} {self.current_bid}"

class Bid(models.Model):
    user = models.ForeignKey(User, on_delete=models.RESTRICT, related_name="bid_user")
    bid = models.FloatField(default=0)
    listing = models.ForeignKey(Listing,blank=False, on_delete=models.CASCADE, related_name="bids")

    def __str__(self):
        return f"{self.bid} {self.listing} {self.user}"

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.RESTRICT, related_name="comment_user")
    comment = models.TextField()
    listing = models.ForeignKey(Listing, blank=False, on_delete=models.RESTRICT, related_name='comments')
    
    def __str__(self):
        return f"{self.user}: {self.comment}"

