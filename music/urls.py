from django.urls import path
from .views import ListSongViews


urlpatterns = [
    path('songs/', ListSongViews.as_view(), name="songs-all")
]