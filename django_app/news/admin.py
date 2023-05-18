from django.contrib import admin
from .models import News, Category

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'created_at', 'updated_at', 'is_published')  # название полей в админке
    list_display_links = ('id', 'title') # название полей в админке в виде ссылки
    search_fields = ('title', 'content') # поиск по этим полям в админке
    list_editable = ('is_published',) # редактирование из админки, не открывая новость
    list_filter = ('is_published', 'category')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')  # название полей в админке
    list_display_links = ('id', 'title') # название полей в админке в виде ссылки
    search_fields = ('title',) # поиск по этим полям в админке

admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)

