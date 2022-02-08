from django.contrib import admin

from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'realtors')
    list_per_page = 25
    list_editable = ('is_published',)
    list_filter = ('realtors',)
    list_display_links = ('title',)
    search_fields = ('id', 'title', 'description', 'address', 'city', 'state', 'zipcode', 'price')

# Register your models here.
admin.site.register(Listing, ListingAdmin)