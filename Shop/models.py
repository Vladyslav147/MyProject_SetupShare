from django.db import models
from django.conf import settings
from django.urls import reverse
# Create your models here.

class Announcement(models.Model):
    STATUS_CHOICES = [
        ('used', 'Б/У'),
        ('new', 'Новое'),
        ('average', 'Среднее'),
        ('spareparts', 'На запчасти'),
    ]
    STATUS_CHOICES_COMPONENTS = [
        ('gpu', 'Видеокарта'),
        ('cpu', 'Процессор'),
        ('psu', 'Блок питания'),
        ('ram', 'Оперативка'),
        ('motherboard', 'Материнская плата'),
        ('cooler','Охлаждение'),
        ('case', 'Корпус'),
        ('ssd', 'SSD'),
        ('monitor', 'Монитор'),
        ('keyboard', 'Клавиатура'),
        ('others', 'Другое')
    ]
    
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    main_photo = models.ImageField(upload_to='Shop/main_photo')
    title = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    price = models.IntegerField()
    phone = models.IntegerField()
    state = models.CharField(max_length=20, choices=STATUS_CHOICES, default='used')
    state_components = models.CharField(max_length=20, choices=STATUS_CHOICES_COMPONENTS, default='others')
    manufacture = models.CharField(max_length=100)
    guarantee = models.CharField(max_length=100)
    complete = models.CharField(max_length=100)
    description = models.TextField()
    created_to = models.DateTimeField(auto_now_add=True)

    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like')

    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-created_to']

    def get_absolute_url(self):
        return reverse("Shop:detail-product", kwargs={"pk": self.pk})
    
class PhotoAnnouncement(models.Model):
    announcement = models.ForeignKey(Announcement, on_delete=models.CASCADE, related_name='additional_photo')
    photo = models.ImageField(upload_to='Shop/additional_photo', blank=True, null=True)