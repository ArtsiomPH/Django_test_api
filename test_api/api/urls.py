from django.urls import path, include
from .views import UserViewSet

from rest_framework import routers

router = routers.SimpleRouter()
router.register(prefix=r"users", viewset=UserViewSet)

urlpatterns = [
    path('v1/api-auth/', include('rest_framework.urls')),
    path('v1/', include(router.urls)),
]