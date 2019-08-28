from rest_framework import generics
from .models import Song
from .serializers import SongSerializer
# Create your views here.


class ListSongViews(generics.ListAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer