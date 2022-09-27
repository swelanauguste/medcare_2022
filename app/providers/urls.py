from django.urls import path

from . import views

app_name = "providers"

urlpatterns = [
    path("", views.ProviderListView.as_view(), name="provider-list"),
    path("detail/<int:pk>/", views.ProvideDetailView.as_view(), name="provider-detail"),
]
