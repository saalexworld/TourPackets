from rest_framework.routers import DefaultRouter

from .views import PacketViewSet, CategoryViewSet, PacketImageViewSet, HotelViewSet


router = DefaultRouter()
router.register('packets', PacketViewSet, basename='packets')
router.register('image_packets', PacketImageViewSet, basename='image_packets')
router.register('categories', CategoryViewSet, basename='categories')
router.register('hotels', HotelViewSet, basename='hotels')

urlpatterns = router.urls
