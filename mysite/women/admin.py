from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *


# @admin.register(Women)
class WomenAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'get_html_photo', 'is_published')  # список полей в админпанели
    list_display_links = ('id', 'title')  # поля-ссылки
    search_fields = ('title', 'content')  # поля для поиска
    list_editable = ('is_published',)  # поля с возможностью редактирования в админпанели
    list_filter = ('is_published', 'time_create')  # поля для фильтрации
    prepopulated_fields = {'slug': ('title',)}  # поля для автоматического заполнения по выбранному полю
    fields = ('title', 'slug', 'cat', 'content', 'photo', 'get_html_photo', 'is_published', 'time_create', 'time_update')
    readonly_fields = ('time_create', 'time_update', 'get_html_photo')
    save_on_top = True

    def get_html_photo(self,  object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50>")
        
    get_html_photo.short_description = 'Фото'


# @admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Women, WomenAdmin)
admin.site.register(Category, CategoryAdmin)

admin.site.site_title = 'Админ-панель сайта о женщинах'
admin.site.site_header = 'Админ-панель сайта о женщинах'
