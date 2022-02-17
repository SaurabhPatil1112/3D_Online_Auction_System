from django.contrib import admin
from .models import Category, AuctionListing, User, Comment, Bid,UserDetails

# Register your models here.
admin.site.register(User)
admin.site.register(Category)
admin.site.register(AuctionListing)
admin.site.register(Bid)
admin.site.register(Comment)
admin.site.register(UserDetails)
