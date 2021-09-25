from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("createListing", views.create_listing, name='create_listing'),
    path("listing/<int:id>", views.listing_page, name='listing'),
    path("listing/addbid/<int:id>", views.add_bid, name='add_bid'),
    path("watchlist", views.watchlist, name="watchlist"),
    path("addwatchlist/<int:id>", views.add_watchlist, name="add_watchlist"),
    path("removewatchlist/<int:id>", views.remove_watchlist, name="remove_watchlist"),
    path("categories", views.categories_index, name="categories"),
    path("category/<int:id>", views.category, name="category"),
    path("addcomment/<int:id>", views.add_comment, name="add_comment")
]
