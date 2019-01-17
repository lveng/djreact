from django.contrib import admin

# Register your models here.

from .models import Article, Ders, Sinif, DersKayit

admin.site.register(Article)
admin.site.register(Ders)
admin.site.register(Sinif)
admin.site.register(DersKayit)
