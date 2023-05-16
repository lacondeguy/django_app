from django.contrib import admin
from django.urls import path, include
from news.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('news.urls')),
]


