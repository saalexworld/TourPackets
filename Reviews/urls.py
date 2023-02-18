from rest_framework.routers import DefaultRouter

from .views import RatingViewSet, CommentViewSet


router = DefaultRouter()
router.register('ratings', RatingViewSet, basename='ratings')
router.register('comments', CommentViewSet, basename='comments')

urlpatterns = router.urls