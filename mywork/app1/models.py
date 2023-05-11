from django.db import models
from django.urls import reverse
from django.core.validators import FileExtensionValidator
class students(models.Model):
    title = models.CharField(max_length=255,verbose_name="Заголовок")  # ,второй аргумент используется Админ панеле
    photo = models.ImageField(upload_to="photos/%Y/%m/%d",verbose_name="Фото")
    time_create = models.DateTimeField(auto_now_add=True,verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True,verbose_name="Время Изменения")
    cat = models.ForeignKey('categ',on_delete=models.PROTECT,null=True,verbose_name="Категория")
    # для ImageField необходимо определит и настроит  MEDIA_ROOT и MEDIA_URL
    def __str__(self):
        return self.title

    def get_absolute_url(self):                                # Админ панеле появится
        return reverse('post',kwargs={'post_id': self.pk})     #  кнопка 'смотреть на сайте'

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии' # Множественное число
        ordering = ['time_create', 'title']

#    class meta:                                    #  TODO Шу
#        verbose_name = u'Фотографии'                #  ишламаяпти  (Meta булиши керак экан (meta эмас))
#        verbose_name_plural = 'Фотографии'         # Админ панелида Students чикяпти
#        ordering = ['time_create','title']         # 'Фотографии однакурсников' чикиши керак эди

class categ(models.Model):
    name = models.CharField(max_length=100, db_index=True,verbose_name="Категория")  # ,второй аргумент используется Админ панеле

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'   # Множественное число
        ordering = ['id']

#=====================================================
class video(models.Model):
    title = models.CharField(max_length=255,verbose_name="Заголовок")  # ,второй аргумент используется Админ панеле
    videofile = models.FileField(
        upload_to= 'video/',verbose_name='Видео',validators=[FileExtensionValidator(allowed_extensions=['mp4'])]
    )
    time_create = models.DateTimeField(auto_now_add=True,verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True,verbose_name="Время Изменения")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео' # Множественное число
        ordering = ['time_create', 'title']

#    class meta:                                    #  TODO Шу
#        verbose_name = u'Фотографии'                #  ишламаяпти  (Meta булиши керак экан (meta эмас))
#        verbose_name_plural = 'Фотографии'         # Админ панелида Students чикяпти
#        ordering = ['time_create','title']         # 'Фотографии однакурсников' чикиши керак эди
