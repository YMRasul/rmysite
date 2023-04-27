from django.contrib import admin
from django.urls import path,include
#from app1.views import index  #1-вариант
from app1.views import *       #2-вариант

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('app1.urls')),   # Создать файл urls.py в папке app1
]
'''
ниже,
мы обработчику 404 (handler404) т.е. обработчику django 
указали использовать нашу функцию pageNotFound
для отображение несушествующих страниц 
'''
handler404 = pageNotFound # обработчик для страницы 404
                          # функцию pageNotFound добавим в app1.views.py

'''
Аналогичным образом можно переопределить
handler500 - ошибка сервера
handler403 - доступ запрещен
handler400 - невозможно обработат запрос

Все эти обработчики начинают работат, когда DEBUG=False
https://djbook.ru/rel3.0/topics/http/views.html
'''