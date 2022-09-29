from django.views.generic import ListView

from .models import Job


class JobListView(ListView):
    model = Job
