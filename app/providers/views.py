from django.views.generic import CreateView, DetailView, ListView, UpdateView

from .models import Provider


class ProviderListView(ListView):
    model = Provider


class ProvideDetailView(DetailView):
    model = Provider


class ProviderUpdateView(UpdateView):
    model = Provider
    fields = "__all__"
