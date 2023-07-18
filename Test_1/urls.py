from .views import TaskAPIView, CommentAPIView, ProjectAPIView
from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter()
router.register(r'task', TaskAPIView, basename='post')
router.register(r'comment', CommentAPIView, basename='comment')
router.register(r'project', ProjectAPIView, basename='project')


urlpatterns = [
    # path('post/', PostAPIView.as_view({'get': 'list'})),
    # path('comment/', CommentAPIView.as_view({'get': 'list'})),
    path('', include(router.urls)),
]