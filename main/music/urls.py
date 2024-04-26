from music.views import MusicApiList, MusicRetrieveList, MusicApiCreate, GenreApiList, GenreRetrieveList
from django.urls import path

urlpatterns = [
    path('music/', MusicApiList.as_view()),
    path('music/<int:pk>/', MusicRetrieveList.as_view()),
    path('music/create/', MusicApiCreate.as_view()),
    path('genre/', GenreApiList.as_view()),
    path('genre/<int:pk>/', GenreRetrieveList.as_view())
]
