from django.contrib import admin
from .models import Course, Category, Review



@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "slug", "category", "creation")
    list_display_links = ("id", "title")
    search_fields = ("title", "category")
    list_filter = ("title", "slug", "category")
    list_per_page = 100


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("id", "name")
    search_fields = ("name", "name")
    # list_filter = ("name", )
    list_per_page = 100


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("id", "course", "name", "review", "creation")
    list_display_links = ("id", "name", "course")
    search_fields = ("name", "course")
    list_filter = ("name", "course")
    list_per_page = 100

