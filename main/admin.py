from django.contrib import admin

from .models import Listing, LikedListing

# Register your models here.
class LikedListing(admin.ModelAdmin):
    readonly_fields = ('id',)


class ListingAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)


admin.site.register(LikedListing, LikedListingAdmin)
admin.site.register(Listing, ListingAdmin)

