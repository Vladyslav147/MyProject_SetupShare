from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Tag, SetupPosts
from users.models import CustomRegisterUser


admin.site.register(CustomRegisterUser)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name',)

@admin.register(SetupPosts)
class SetupPostsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'get_html_photo', 'cpu', 'gpu', 'creator')# Что мы видим в списке всех постов

    list_display_links = ('id', 'title')# На что можно нажать, чтобы перейти в пост

    search_fields = ('title', 'cpu', 'gpu', 'comment')# Поля, по которым можно искать (очень удобно!)

    list_filter = ('creator',)    # Фильтр справа (например, по автору)

    filter_horizontal = ('tegs',) # удобный виджет для выбора тегов (перекидывание из левого окна в правое)

    # Функция для вывода маленького превью картинки прямо в списке
    def get_html_photo(self, object):
        if object.main_photo:
            return mark_safe(f"<img src='{object.main_photo.url}' width=50>")
        return "Нет фото"

    get_html_photo.short_description = "Превью"