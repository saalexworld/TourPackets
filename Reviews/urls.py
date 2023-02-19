from rest_framework.routers import DefaultRouter

from .views import RatingViewSet, CommentViewSet, FavoriteViewSet


router = DefaultRouter()
router.register('ratings', RatingViewSet, basename='ratings')
router.register('comments', CommentViewSet, basename='comments')
router.register('favorits', FavoriteViewSet, basename='favorits')

urlpatterns = router.urls
