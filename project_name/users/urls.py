from django.conf.urls import include
from django.urls import path
from djoser.views import UserViewSet
from rest_framework import routers

from project_name.users.viewsets import PermissionViewSet, GroupViewSet

router = routers.SimpleRouter()

router.register('permission', PermissionViewSet)
router.register('group', GroupViewSet)
router.register('users', UserViewSet)

urlpatterns = router.urls

urlpatterns += [
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls.jwt'))
]
