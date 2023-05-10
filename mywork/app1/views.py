from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import students,categ

# AAA menu = ["О сайте", "Добавить", "Обратная связь", "Войти"]

menu = [{'title': "О сайте",        'url_name': 'about'}]  # Это после добавление 'Регистрация|Войти' в файле base.html

def index(request):
    #stdns = students.objects.all()        # Все фотографии
    stdns = students.objects.filter(pk=1) # только одна фотография
    cats = categ.objects.all()
    cntxt ={
        'stdns': stdns,
        'cats': cats,
        'menu': menu,
        'title': 'ТашГУ матфак82',
        'cat_selected': 0,
    }
    # AAA return render(request, 'app1/index.html', {'stdns': stdns, 'menu': menu, 'title': 'Главная страница'})
    return render(request, 'app1/index.html', context=cntxt)
# третьим аргументом передаем словарь cntxt
#
def show_category(request,cat_id):
    stdns = students.objects.filter(cat_id=cat_id)
    cats = categ.objects.all()
    if len(stdns) == 0:
        raise Http404()
    cntxt = {
            'stdns': stdns,
            'cats': cats,
            'menu': menu,
            'title': 'ТашГУ матфак82',
            'cat_selected': cat_id,
    }
    return render(request, 'app1/index.html', context=cntxt)
#
def about(request):
    return render(request, 'app1/about.html', {'menu': menu, 'title': 'О сайте'})

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')  # должны импортировать эту функцию

