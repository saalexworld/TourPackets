# from django.views.decorators.cache import cache_page
# from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import PacketViewSet, CategoryViewSet, PacketImageViewSet, HotelViewSet

# urlpatterns = [
#     path('packets/', cache_page(60) (PacketViewSet.as_view()), name='packets'),
#     path('image_packets/', PacketImageViewSet.as_view(), name='image_packets'),
#     path('categories/', CategoryViewSet.as_view(), name='categories'),
#     path('hotels/', HotelViewSet.as_view(), name='hotels'),
# ]

router = DefaultRouter()
router.register('packets', PacketViewSet, basename='packets')
router.register('image_packets', PacketImageViewSet, basename='image_packets')
router.register('categories', CategoryViewSet, basename='categories')
router.register('hotels', HotelViewSet, basename='hotels')

urlpatterns = router.urls
