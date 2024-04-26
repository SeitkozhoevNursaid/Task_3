from django.contrib import admin
from music.models import Genre, Music, MusicImg
# Register your models here.

admin.site.register(Music)
admin.site.register(Genre)
admin.site.register(MusicImg)
