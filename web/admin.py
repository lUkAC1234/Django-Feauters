from django.contrib import admin
from .models import UserModel, BlogModel, BlogCategoryModel, FunctionsModel
from django.utils.translation import gettext_lazy as _
# For saving html code
from django.utils.safestring import mark_safe


# --------------------------------------------------------------------------- #
# User Model Admin
@admin.register(UserModel)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username']
    list_display_links = ['id', 'username']
    search_fields = ['username']

@admin.register(BlogModel)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['id', 'title']
    search_fields = ['title']

@admin.register(BlogCategoryModel)
class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'category']
    list_display_links = ['id', 'category']
    search_fields = ['category']

@admin.register(FunctionsModel)
class FunctionsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['id', 'title']
    search_fields = ['title']

admin.site.site_header = 'Django Feautures'
admin.site.site_title = 'Django Feautures'