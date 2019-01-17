
from rest_framework import serializers
from articles.models import Article, Ders, Sinif, DersKayit

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'content')


class DersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ders
        fields = ('id', 'adi', 'aciklama')


class SinifSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sinif
        fields = ('id', 'adi', 'aciklama')


class DersKayitSerializer(serializers.ModelSerializer):
    class Meta:
        model = DersKayit
        fields = ('id', 'ders', 'sinif', 'baslangic', 'bitis')
