from django.urls import path, re_path
from mywork import settings
from django.conf.urls.static import static
from .views import *
'''
urlpatterns=[
    path('',index),
    path('cats/<int:idcat>/', categ),
    re_path(r'^arhive/(?P<year>[0-9]{4})/', arh), # регулярное выражения
]
'''

'''
# исправление views.[n1] ,name='home' home придумаем мы сами
urlpatterns=[
    path('',index,name='home'),
    path('cats/<int:idcat>/', categ),
    re_path(r'^arhive/(?P<year>[0-9]{4})/', arh), # регулярное выражения
]
'''
# исправление views.[n2] name='home' home придумаем мы сами
urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('add_page/', addpage, name='add_page'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('post/<int:post_id>/', show_post, name='post'),
    path('category/<int:cat_id>/', show_category, name='category'),

]

# Добавление  [n3] от mywork.setttins
if settings.DEBUG:  # from mywork import settings
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    #  для static from django.conf.urls.static import settings

handler404 = pageNotFound
