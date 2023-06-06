from django.shortcuts import render
from django.http import HttpResponse
from .models import News, Category



def index(request):
    news = News.objects.order_by('-created_at')
    categories = Category.objects.all()

    context = {
        'news_example': news,
        'title': 'Все новости',
        'categories': categories,
    }
    return render(request, template_name='news/index.html', context=context)


def get_category(request, category_id):
    news = News.objects.filter(category_id = category_id)
    categories = Category.objects.all()
    category = Category.objects.get(pk=category_id)
    return render(request, 'news/category.html', {'news_example': news, 'categories': categories, 'category': category })

