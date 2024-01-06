from django.db import models
from users.models import MyUser

class photos(models.Model):
    title = models.CharField("Название", max_length=255)
    author = models.TextField("Автор")
    photo = models.ImageField("Фото", upload_to='user_image', null=True, default=None)

    def __str__(self):
        return f'Фото:{self.title}'

    def get_sum_rating(self):
        return sum([rating.value for rating in self.ratings.all()])

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фото'

    def all(self):
        return self.get_queryset().select_related('author', 'title').prefetch_related('ratings').filter(
                status='published')

class Rating(models.Model):
    """
    Модель рейтинга: Лайк - Дизлайк
    """
    article = models.ForeignKey(photos, verbose_name='Статья', on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(MyUser, verbose_name='Пользователь', on_delete=models.CASCADE, blank=True, null=True)
    value = models.IntegerField(verbose_name='Значение', choices=[(1, 'Нравится'), (-1, 'Не нравится')])

    class Meta:
        ordering = ('-id',)
        indexes = [models.Index(fields=['value'])]
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'

    def get_sum_rating(self):
        return sum([rating.value for rating in self.ratings.all.filter()])

    def all(self):
        """
        Список статей (SQL запрос с фильтрацией для страницы списка статей)
        """
        return self.get_queryset().select_related('author', 'title').prefetch_related('ratings').filter(
            status='published')

    def detail(self):
        """
        Детальная статья (SQL запрос с фильтрацией для страницы со статьёй)
        """
        return self.get_queryset() \
            .select_related('author', 'title') \
            .prefetch_related('ratings') \
            .filter(status='published')

