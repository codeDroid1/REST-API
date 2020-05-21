from django.urls import path, include
from rest_framework import routers
from api.views import StudentViewSet, SchoolViewSet

router = routers.DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'schools', SchoolViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/v1', include('rest_framework.urls', namespace='rest_framework')),
]
