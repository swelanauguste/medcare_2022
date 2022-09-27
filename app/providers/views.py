from django.views.generic import CreateView, DetailView, ListView

from .models import Provider


class ProviderListView(ListView):
    model = Provider


class ProvideDetailView(DetailView):
    model = Provider
