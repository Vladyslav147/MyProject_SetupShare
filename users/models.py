from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
class CustomRegisterUser(AbstractUser):
    phone = models.CharField(max_length=12, verbose_name='Номер телефона')

    def __str__(self):
        return self.username
    
class BioUsers(models.Model):
    creator = models.OneToOneField(CustomRegisterUser, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatar', null=True, blank=True, verbose_name='Аватар')
    background_image = models.ImageField(upload_to='background_image', null=True, blank=True, verbose_name='Фоновое изображение')
    first_name = models.CharField(max_length=10, verbose_name='Имя пользователя')
    profission = models.CharField(max_length=30, null=True, blank=True, verbose_name='Професия')
    bio = models.CharField(max_length=255, null=True, blank=True, verbose_name='Биография')

    Instagram_url = models.URLField(null=True, blank=True, verbose_name='Ссылка на Instagram')
    github_url = models.URLField(null=True, blank=True, verbose_name='Ссылка на GitHub')
    discord_url = models.URLField(max_length=35, null=True, blank=True, verbose_name='Ссылка на Discord канал')
    steam_url = models.URLField(max_length=255, null=True, blank=True, verbose_name='Ссылка на steam')
    telegram_url = models.URLField(max_length=100, null=True, blank=True, verbose_name='Ссылка на telegram')
    spotify_url = models.URLField(max_length=100, null=True, blank=True, verbose_name='Ссылка на spotify плейлист')
    tiktok_url = models.URLField(max_length=100, blank=True, null=True, verbose_name='Ссылка на ТТ')

    def __str__(self):
        return self.creator.username


#Потом эту логику сигналов для нее создать отдельный файл
@receiver(post_save, sender=CustomRegisterUser)
def manage_user_profile(sender, instance, created, **kwargs):
    if created:
        BioUsers.objects.create(creator=instance)