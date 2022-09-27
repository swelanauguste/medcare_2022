from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("providers.urls", namespace="providers")),
    path("admin/", admin.site.urls),
]
