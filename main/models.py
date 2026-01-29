from django.db import models
from SetupShere import settings
# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название тега')
    def __str__(self):
        return self.name
    
class SetupPosts(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название поста')

    main_photo = models.ImageField(upload_to='main_photo')
    more_photo1 = models.ImageField(upload_to='morePhoto1', blank=True, null=True)
    more_photo2 = models.ImageField(upload_to='morePhoto2', blank=True, null=True)
    more_photo3 = models.ImageField(upload_to='morePhoto3', blank=True, null=True)

    cpu = models.CharField(max_length=20, verbose_name='CPU')
    gpu = models.CharField(max_length=20, verbose_name='GPU')
    ram = models.CharField(max_length=20, verbose_name='RAM')
    ssd = models.CharField(max_length=30, verbose_name='Накопитель')
    monitor = models.CharField(max_length=30, verbose_name='Монитор')
    ps = models.CharField(max_length=30, blank=True, null=True, verbose_name='Блок питания')
    comment = models.CharField(max_length=100, verbose_name='Дополнение')
    story_setup = models.TextField(blank=True, null=True, verbose_name='История Сборки')
    tegs = models.ManyToManyField(Tag, blank=True, verbose_name='Теги')

    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


