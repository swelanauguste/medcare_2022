from django.contrib import admin

from .models import Job, Tag

admin.site.register(Tag)
admin.site.register(Job)
