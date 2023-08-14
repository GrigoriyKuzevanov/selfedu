from django.http import Http404, HttpResponse, HttpResponseNotFound
from django.shortcuts import get_object_or_404, redirect, render
from .models import *


menu = [
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Добавить статью', 'url_name': 'add_page'},
    {'title': 'Обратная связь', 'url_name': 'contacts'},
    {'title': 'Войти', 'url_name': 'login'},
]

def index(request):
    posts = Women.objects.all()

    context = {
        'posts': posts,
        'title': 'Главная страница',
        'cat_selected': 0,
    }
    return render(request, 'women/index.html', context=context)

def about(request):
    return render(request, 'women/about.html', {'menu': menu, 'title': 'О сайте'})

def addpage(request):
    return HttpResponse('Здесь будет раздел "Добавить страницу"!')

def contacts(request):
    return HttpResponse('Здесь будет раздел "Контакты"!')

def login(request):
    return HttpResponse('Здесь будет раздел "Login"!')

def show_post(request, post_id):
    post = get_object_or_404(Women, pk=post_id)
    
    context = {
        'post': post,
        'menu': menu,
        'title': post.title,
        'cat_selected': post.cat_id,
    }
    return render(request, 'women/post.html', context=context)

def show_category(request, cat_id):
    posts = Women.objects.filter(cat_id=cat_id)

    if len(posts) == 0:
        raise Http404()

    context = {
        'posts': posts,
        # 'menu': menu,
        'title': 'Отображение по рубрикам',
        'cat_selected': cat_id,
    }
    return render(request, 'women/index.html', context=context)

# def categories(request, catid):
#     if request.GET:
#         print(request.GET)
#     return HttpResponse(f'<h1>Статьи по категориям</h1><p>{catid}</p>')

# def archive(request, year):
#     if int(year) > 2020:
#         return redirect('home', permanent=True)
#     return HttpResponse(f'<h1>Архив по годам</h1><p>{year}</p>')

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
