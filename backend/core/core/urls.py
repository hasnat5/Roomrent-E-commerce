from django.contrib import admin
from django.urls import path,include, re_path
from . import views
from rest_framework.schemas import get_schema_view
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Roomrent API Documentation",
        default_version='v1',
        description="Documentation",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('',include('buyer.urls')),
    path('login/',views.login),
    path('accounts/', include('allauth.urls'), name='social'),
    path('admin/', admin.site.urls),
    path('api_documentation/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^api_documentation(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),    
    path('auth/',include('api.authentication.urls')),
    path('account/',include('api.account.urls')),
    path('seller/home/',include('seller.urls')),
    path('product/',include('api.product.urls')),
]