from django.contrib import admin
from users.models import CustomUser

class ListingUsers(admin.ModelAdmin):
    list_display = ("id", "username")
    list_display_links = ("id", "username")
    search_fields = ("username", )
    # list_filter = ("is_admin", )
    list_per_page = 20

admin.site.register(CustomUser, ListingUsers)



