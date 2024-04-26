from django.db import models
from login.models import CustomUser
from django.db.models.signals import post_delete, post_save
from changelog.mixins import ChangeloggableMixin
from changelog.signals import journal_save_handler, journal_delete_handler
# Create your models here.


class Genre(models.Model):
    name = models.CharField(verbose_name='Жанр музыки', max_length=50)
    
    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.name


class Music(ChangeloggableMixin, models.Model):
    name = models.CharField(
        verbose_name='Название песни', max_length=50
    )
    genre = models.ForeignKey(
        Genre, verbose_name='Жанр',
        on_delete=models.CASCADE, related_name='music'
    )
    user = models.ForeignKey(
        CustomUser, verbose_name='Пользователь',
        on_delete=models.CASCADE, related_name='musics'
    )
    author = models.CharField(
        verbose_name='Автор', max_length=50
    )
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Песня'
        verbose_name_plural = 'Песни'

    def __str__(self):
        return self.name


class MusicImg(models.Model):
    images = models.FileField(upload_to='images/')
    music = models.ForeignKey(Music, on_delete=models.CASCADE, related_name='images')

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'


post_save.connect(journal_save_handler, sender=Music)
post_delete.connect(journal_delete_handler, sender=Music)
