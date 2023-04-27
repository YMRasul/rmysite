from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import students,categ

# Create your views here.
''' вместе этого можем организовать в виде шаблона
def index(request):
    return HttpResponse("<h1>Главная страница</h1>")
'''
'''
def index(request):
    return render(request,'app1/index.html') # render шаблонизатор, второй аргумент путь к шаблону

def about(request):
    return render(request,'app1/about.html') # добавим маршрут для этой функции
# в app1.urls.py исправить [n2]
'''
# AAA menu = ["О сайте", "Добавить", "Обратная связь", "Войти"]
menu = [{'title': "О сайте",        'url_name': 'about'},
        {'title': "Добавить",       'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти",          'url_name': 'login'}
]

def index(request):
    #stdns = students.objects.all()        # Все фотографии
    stdns = students.objects.filter(pk=1) # только одна фотография
    cats = categ.objects.all()
    cntxt ={
        'stdns': stdns,
        'cats': cats,
        'menu': menu,
        'title': 'Главная страница',
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
            'title': 'Главная страница',
            'cat_selected': cat_id,
    }
    return render(request, 'app1/index.html', context=cntxt)
#
def about(request):
    return render(request, 'app1/about.html', {'menu': menu, 'title': 'О сайте'})


def addpage(request):
    return HttpResponse("Добавление статьи")


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")

def show_post(request,post_id):
    return HttpResponse(f"Отображение статьи с id  = {post_id}")

#def show_category(request,cat_id):
#    return HttpResponse(f"Отображение категории с id = {cat_id} ")

#
#
'''
    def categ(request, idcat):
        if request.GET:
            print(request.GET)
        return HttpResponse(f"<h2>Страница категории</h2><p>{idcat}</p>")
    def arh(request, year):
        if int(year) > 2020:
            # raise Http404()  # Http404 должны импортировать
            '' '
            вместо этого можем использовать redirect
            и это должны импортировать
            '' '
            # return redirect('/') # Временный redirect
            # return redirect('/',permanent=True) # Постоянный redirect (это плохой код)
            return redirect('home', permanent=True)  # Постоянный redirect (это хороший тон)
            # в app1.urls.py исправить [n1]
            '' '
            если без return то перенаправление не будеть
            '' '
        return HttpResponse(f"<h2>Архив по годам</h2><p>{year}</p>")
'''

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')  # должны импортировать эту функцию
