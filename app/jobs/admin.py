from django.contrib import admin

from .models import Job, Tag, SkillLevel

admin.site.register(Tag)
admin.site.register(Job)
admin.site.register(SkillLevel)
