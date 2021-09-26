from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django import forms
from django.db.models import Max

from .models import User, Listing, Comment, Bid, Category
 
#Forms
class CreateListingForm(forms.Form):
    title = forms.CharField(label='title', widget=forms.TextInput(attrs={'class':'formfield'}))
    description = forms.CharField(label=False, widget=forms.Textarea(attrs={'class':'formfield', 'placeholder':'Description'}))
    starting_bid = forms.FloatField(label='Starting Bid', widget=forms.TextInput(attrs={'class':'formfield'}))
    image = forms.URLField(label='Image Url', widget=forms.TextInput(attrs={'class':'formfield'}))
        
#views
def index(request):
    return render(request, "auctions/index.html",{
        "Listings": Listing.objects.exclude(is_active = False).all(),
        "header" : "Active Listings"
    })

def closed_listings(request):
    return render(request, "auctions/index.html",{
        "Listings": Listing.objects.exclude(is_active = True).all(),
        "header" : "Closed Auctions"
    })

def listing_page(request, id):
    current_user = request.user
    if request.user.is_authenticated:
        watchlist = current_user.watchlist_users.all()
    else:
        watchlist = None
    listing = Listing.objects.get(pk=id)
    comments = listing.comments.all()
    if listing.bids.all():
        max_bid_value = list(listing.bids.all().aggregate(Max('bid')).values())[0]
        max_bid = Bid.objects.get(bid = max_bid_value, listing=listing)
        bid_user = max_bid.user
        return render(request, "auctions/listing.html",{
            "listing": listing,
            "max_bid": max_bid_value,
            "bid_user": bid_user,
            "current_user": current_user,
            "watchlist": watchlist,
            "comments" : comments
        })
    listing.number_of_bids = 0
    listing.current_bid = listing.starting_bid
    listing.save()
    return render(request, "auctions/listing.html",{
        "listing": listing,
        "max_bid": 0,
        "bid_user": None,
        "current_user": request.user,
        "watchlist": watchlist,
        "comments" : comments
    })

def add_bid(request,id):
    if request.method == 'POST':
        listing = Listing.objects.get(pk=id)
        bid = request.POST['bid']
        current_user = request.user
        new_bid = Bid(user = current_user, bid = bid , listing = listing)
        new_bid.save()
        max_bid = list(listing.bids.all().aggregate(Max('bid')).values())[0]
        listing.current_bid = max_bid
        listing.number_of_bids = listing.number_of_bids + 1
        listing.save()
        return HttpResponseRedirect(reverse("listing", args=(listing.id,)))


def create_listing(request):
    if request.method == 'POST':
        current_user = request.user
        form = CreateListingForm(request.POST)
        category = Category.objects.get(pk=int(request.POST['category']))
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            startingBid = form.cleaned_data['starting_bid']
            img = form.cleaned_data['image']
        new_listing = Listing(user = current_user, title = title, description=description, starting_bid = startingBid, image=img, category = category, winner = request.user)
        new_listing.save()
        return HttpResponseRedirect(reverse("index"))
    categories = Category.objects.all()
    return render(request, "auctions/createListing.html",{
        "form" : CreateListingForm(),
        "categories": categories
    })

def close_listing(request, id):
    if request.method == 'POST':
        current_user = request.user
        listing = Listing.objects.get(pk=id)
        max_bid_value = list(listing.bids.all().aggregate(Max('bid')).values())[0]
        max_bid = Bid.objects.get(bid = max_bid_value, listing=listing)
        bid_user = max_bid.user
        listing.winner = bid_user
        listing.is_active = False
        listing.save()
        return HttpResponseRedirect(reverse("listing", args=(listing.id,)))

def watchlist(request):
    current_user = request.user
    listings = current_user.watchlist_users.all()
    return render(request, "auctions/watchlist.html",{
        "Listings": listings,
    })

def add_watchlist(request, id):
    current_user = request.user
    listing = Listing.objects.get(pk=id)
    current_user.watchlist_users.add(listing)
    return HttpResponseRedirect(reverse("listing", args=(listing.id,)))

def remove_watchlist(request, id):
    current_user = request.user
    listing = Listing.objects.get(pk=id)
    current_user.watchlist_users.remove(listing)
    return HttpResponseRedirect(reverse("listing", args=(listing.id,)))

def categories_index(request):
    categories = Category.objects.exclude(category="No Category").all()
    return render(request, "auctions/categories.html",{
        "categories": categories
    })

def category(request, id):
    if request.method == 'POST':   
        category = Category.objects.get(pk=id)
        listings = category.listings_category.all()
        return render(request, "auctions/category_listing.html",{
        "Listings": listings,
        "category" : category
    })

def add_comment(request, id):
    if request.method == 'POST':
        user = request.user
        listing = Listing.objects.get(pk=id)
        comment = request.POST['comment'] 
        new_comment = Comment(user=user, comment=comment, listing=listing)
        new_comment.save()
        return HttpResponseRedirect(reverse("listing", args=(listing.id,)))


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
