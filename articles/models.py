from django.db import models
import datetime




class Article(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    def __str__(self):
        return self.title


class Ders(models.Model):
    adi = models.CharField(max_length=120)
    aciklama = models.TextField()
    def __str__(self):
        return self.adi


class Sinif(models.Model):
    adi = models.CharField(max_length=120)
    aciklama = models.TextField()
    def __str__(self):
        return self.adi


class DersKayit(models.Model):
    ders = models.ForeignKey(Ders, on_delete=models.PROTECT)
    sinif = models.ForeignKey(Sinif, on_delete=models.PROTECT)
    baslangic = models.DateTimeField(default=datetime.datetime.now())
    bitis = models.DateTimeField(default=datetime.datetime.now())
    def __str__(self):
        return '%s-%s' % (self.ders, self.sinif)
