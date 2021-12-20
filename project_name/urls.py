"""project_name URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/{{ docs_version }}/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings as dj_s
from django.conf.urls import include
from django.urls import path, re_path

urlpatterns = [
    path('api/', include([
        path('', include('project_name.users.urls')),
    ]))
]

if dj_s.ENABLE_OPEN_API_SCHEMA:
    from rest_framework import permissions
    from drf_yasg.views import get_schema_view
    from drf_yasg import openapi

    schema_view = get_schema_view(
        openapi.Info(
            title=dj_s.OPEN_API_TITLE,
            default_version=dj_s.OPEN_API_VERSION,
            description=dj_s.OPEN_API_DESCRIPTION,
            terms_of_service=dj_s.OPEN_API_TERMS_OF_SERVICES,
            contact=openapi.Contact(email=dj_s.OPEN_API_CONTACT),
            license=openapi.License(name=dj_s.OPEN_API_LICENCE),
        ),
        public=True,
        permission_classes=(permissions.AllowAny,),
    )

    if dj_s.OPEN_API_SCHEMA_TYPE == 'swagger':
        urlpatterns += [
            re_path(r'^schema(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
            path('schema/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui')
        ]
    else:
        urlpatterns += [
            path('schema/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc')
        ]
