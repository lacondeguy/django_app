from django.contrib import admin
from .models import News

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'updated_at', 'is_published')  # название полей в админке
    list_display_links = ('id', 'title') # название полей в админке в виде ссылки
    search_fields = ('title', 'content') # поиск по этим полям в админке

admin.site.register(News, NewsAdmin)

