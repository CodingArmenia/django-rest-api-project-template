from django.contrib.auth.models import Permission, Group
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from project_name.users.serializers import PermissionSerializer, GroupSerializer


class PermissionViewSet(viewsets.ModelViewSet):
    queryset = Permission.objects.all()
    permission_classes = [AllowAny]
    serializer_class = PermissionSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    permission_classes = [AllowAny]
    serializer_class = GroupSerializer
