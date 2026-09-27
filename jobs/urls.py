from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import JobViewSet, ApplicationViewSet


router = DefaultRouter()

router.register('jobs', JobViewSet)
router.register('applications', ApplicationViewSet)


urlpatterns = [
    path('', include(router.urls)),
]