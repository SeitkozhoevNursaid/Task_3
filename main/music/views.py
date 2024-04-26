from rest_framework import generics
from music.models import Music, Genre
from music.serializers import MusicSerializer, GenreSerializer
from rest_framework.permissions import IsAuthenticated
from music.permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from music.filters import CustomSearchFilter
from music.pagination import StandartPagination
from django.http import Http404


# Crea your views here.


class MusicApiList(generics.ListAPIView):
    serializer_class = MusicSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = StandartPagination

    def get_queryset(self):    
        queryset = Music.objects.all()
        genre1 = self.request.query_params.get('genre')
        name1 = self.request.query_params.get('name')
        search = self.request.query_params.get('search')
        if genre1:
            queryset = queryset.filter(genre=genre1)
        if name1:    
            queryset = queryset.filter(name=name1)
        if search:
            queryset = queryset.filter(name__icontains=search)
        return queryset


class MusicApiCreate(generics.CreateAPIView):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer
    permission_classes = [IsAuthenticated]


class MusicRetrieveList(generics.RetrieveUpdateDestroyAPIView):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer
    permission_classes = [IsOwnerOrReadOnly]


class GenreApiList(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    
    

class GenreRetrieveList(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
 

# Фильтрация (get_queryset() и django-filters), поиск (get_queryset() и django-filters), сортировка (ordering), пагинация (на глобальном уровне а потом чисто для view), логирование, добавить возможность создавать много картинок к одной песни,
# при создании песни отправлять сообщение тебе на почту что была создана песня и название этой песни (потом подключить CELERY для этого)
# Доделать функции, полностью везде разобраться, что че как выполняется, после переходить к Celery.

# filter_backends = [DjangoFilterBackend, CustomSearchFilter, filters.OrderingFilter]
    # filterset_fields = ['genre',]
    # search_fields = ['^name']
    # ordering_fields = ['created']
    #serializers
