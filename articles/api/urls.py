
from articles.api.views import ArticleViewSet, DersViewSet, SinifViewSet, DersKayitViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'ders', DersViewSet, base_name='ders')
router.register(r'sinif', SinifViewSet, base_name='sinif')
router.register(r'derskayit', DersKayitViewSet, base_name='derskayit')
router.register(r'', ArticleViewSet, base_name='articles')
urlpatterns = router.urls
