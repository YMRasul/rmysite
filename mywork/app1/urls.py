from django.urls import path, re_path
from mywork import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('category/<int:cat_id>/',show_category, name='category'),

]

# Добавление  [n3] от mywork.setttins
if settings.DEBUG:  # from mywork import settings
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    #  для static from django.conf.urls.static import settings

handler404 = pageNotFound
