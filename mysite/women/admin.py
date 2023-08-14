from django.contrib import admin
from .models import *


# @admin.register(Women)
class WomenAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'photo', 'is_published')  # список полей в админпанели
    list_display_links = ('id', 'title')  # поля-ссылки
    search_fields = ('title', 'content')  # поля для поиска
    list_editable = ('is_published',)  # поля с возможностью редактирования в админпанели
    list_filter = ('is_published', 'time_create')  # поля для фильтрации
    prepopulated_fields = {'slug': ('title',)}  # поля для автоматического заполнения по выбранному полю


# @admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Women, WomenAdmin)
admin.site.register(Category, CategoryAdmin)
