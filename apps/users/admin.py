from django.contrib import admin
from .models import CustomUser, UserProfile, UserPreference
from django.contrib.auth.admin import UserAdmin


admin.sites.AdminSite.site_header = 'GuiarMe'
admin.sites.AdminSite.index_title = 'GuiarMe'
admin.sites.AdminSite.site_title = 'Admin Site'


@admin.action(description="Desativar")
def action_desactivate_user(modeladmin, request, queryset):
    for user in queryset:
        user.is_active = False
        user.save()

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ("id", "username", "email", "type_user")
    list_display_links = ("id", "username")
    search_fields = ("username", "email")
    list_filter = ("type_user", )
    list_per_page = 20

    fieldsets = UserAdmin.fieldsets + (
        ('Informações adicionais', {'fields': ('type_user',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Informações adicionais', {'fields': ('type_user',)}),
    )

    actions = [action_desactivate_user]
    # autocomplete_fields = ['']

    # class Media:
    #     js = ('js/')
    #     css = {
    #     'all': ('css/jobs/',)
    #     }


@admin.register(UserPreference)
class UserPreferenceAdmin(admin.ModelAdmin):
    list_display = ("id", "user")
    list_display_links = ("id", )
    search_fields = ("user", )
    list_filter = ("user", )
    list_per_page = 100

@admin.register(UserProfile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "user")
    list_display_links = ("id", "name")
    search_fields = ("name",)
    list_filter = ("sexual_orientation", "user")
    # list_editable = ("publicada",)
    list_per_page = 20
    # autocomplete_fields = ['']

    # class Media:
    #     js = ('js/')
    #     css = {
    #     'all': ('css/jobs/',)
    #     }