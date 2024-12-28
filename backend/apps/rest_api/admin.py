from django.contrib import admin
from apps.rest_api.models import Item

class ListItems(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("id", "name")
    search_fields = ("name",)
    list_filter = ("name",)
    list_per_page = 20
    # list_editable = ("name",)

admin.site.register(Item, ListItems)
