from django.db import models
from django.conf import settings
from django.db.models import Count
from django.urls import reverse
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
    cpu = models.CharField(max_length=20, verbose_name='Процесор')
    gpu = models.CharField(max_length=20, verbose_name='Видеокарта')
    ram = models.CharField(max_length=20, verbose_name='Оперативка')
    ssd = models.CharField(max_length=30, verbose_name='Накопитель')
    monitor = models.CharField(max_length=30, verbose_name='Монитор')
    ps = models.CharField(max_length=30, blank=True, null=True, verbose_name='БП')
    comment = models.CharField(blank=True, null=True, max_length=100, verbose_name='Дополнение')
    story_setup = models.TextField(blank=True, null=True, verbose_name='История Сборки')
    tegs = models.ManyToManyField(Tag, blank=True, verbose_name='Теги', related_name='posts')
    time = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")

    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='post_likes')
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_specs_list(self):
        field_names = ['cpu', 'gpu', 'ram', 'ssd', 'monitor', 'ps']
        specs = []

        for name in field_names:
            label = self._meta.get_field(name)
            value = getattr(self, name)
            
            specs.append({
                'label': label.verbose_name,
                'value': value    
            })
        return specs
    
    # Возвращает всё количество лайков для этого конкретного поста
    def get_total_likes(self):
        return self.likes.count()

    def get_absolute_url(self):
        return reverse("main:detail_post", kwargs={"pk": self.pk})
    
    @property
    def get_comments_count(self):
        return self.comments.count()
    
class CommentPost(models.Model):
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(SetupPosts, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=255)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.text