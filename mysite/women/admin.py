from django.contrib import admin
from .models import *


# @admin.register(Women)
class WomenAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'photo', 'is_published')  # список полей в админпанели
    list_display_links = ('id', 'title')  # поля-ссылки
    search_fields = ('title', 'content')  # поля для поиска
    list_editable = ('is_published',)  # поля с возможностью редактирования в админпанели
    list_filter = ('is_published', 'time_create')  # поля для фильтрации


# @admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


admin.site.register(Women, WomenAdmin)
admin.site.register(Category, CategoryAdmin)
