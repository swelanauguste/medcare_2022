from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("providers.urls", namespace="providers")),
    path("jobs/", include("jobs.urls", namespace="jobs")),
    path("admin/", admin.site.urls),
]
