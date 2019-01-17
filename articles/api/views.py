
from rest_framework import viewsets

from articles.models import Article, Ders, Sinif, DersKayit
from .serializers import ArticleSerializer, DersSerializer, SinifSerializer, DersKayitSerializer

class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()

class DersViewSet(viewsets.ModelViewSet):
    serializer_class = DersSerializer
    queryset = Ders.objects.all()

class SinifViewSet(viewsets.ModelViewSet):
    serializer_class = SinifSerializer
    queryset = Sinif.objects.all()

class DersKayitViewSet(viewsets.ModelViewSet):
    serializer_class = DersKayitSerializer
    queryset = DersKayit.objects.all()
