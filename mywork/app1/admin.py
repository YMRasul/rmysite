from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe

# вспомогательный клас для отображения в админ панеле полей  ('id', 'title', 'time_create', 'photo') #
# после определение этого класса его в 'admin.site.register(students)' добавим вторым аргументом
class studentsAdmin(admin.ModelAdmin):  # students должень совпадат с модели 'students' а Admin для админ панели
    #list_display = ('id', 'title', 'time_create', 'photo')
    list_display = ('id', 'title', 'time_create', 'get_html_photo') # список полей
    list_display_links = ('id', 'title')                            # поля которые мы можем кликнут
    search_fields = ('title',)                                      # поля для поиска
    list_filter = ('time_create',)                                  # поля для фильтрации
    save_on_top = True
    #x Это функция для отображения миниатюра на админ панеле в место пути
    #x в list_display вместо 'photo' пропишем 'get_html_photo'
    def get_html_photo(self,object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50>")

    get_html_photo.short_description = "Миниатюра"
    #x
class categAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    list_display_links = ('id','name')
    search_fields = ('name',)

# 1. Эти регистрации для того чтобы модели нашего приложения видно было в Админ панеле (students,categ)
#    второй параметр добавим после определение классов (studentsAdmin,categAdmin)
admin.site.register(students, studentsAdmin)  # students да туриб  <Alt>+<Enter> ни боссак import чикади
admin.site.register(categ,categAdmin)
#