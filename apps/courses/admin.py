from django.contrib import admin
from .models import Course, Review


class CourseAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "slug")
    list_display_links = ("id", "title")
    search_fields = ("title",)
    list_filter = ("title", "slug")

class ReviewAdmin(admin.ModelAdmin):
    list_display = ("id", "course", "name", "review")
    list_display_links = ("id", "name", "course")
    search_fields = ("name", "course")
    list_filter = ("name", "course")

admin.site.register(Course, CourseAdmin)
admin.site.register(Review, ReviewAdmin)
