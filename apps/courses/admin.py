from django.contrib import admin
from .models import Course, Category, Module, Lesson, Content, Review



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

@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ("id", "course", "title")
    list_display_links = ("id", "title")
    search_fields = ("course", "title")
    # list_filter = ("name", )
    list_per_page = 100

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ("id", "module", "title")
    list_display_links = ("id", "module", "title")
    search_fields = ("module", "module", "title")
    # list_filter = ("name", )
    list_per_page = 100

@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ("id", "lesson")
    list_display_links = ("id", "lesson")
    search_fields = ("lesson", "lesson")
    # list_filter = ("name", )
    list_per_page = 100


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("id", "course", "name", "review", "creation")
    list_display_links = ("id", "name", "course")
    search_fields = ("name", "course")
    list_filter = ("name", "course")
    list_per_page = 100

