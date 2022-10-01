from django.db import models
from providers.models import District, Provider

ENTRY_LEVEL = "entry level"
MID_LEVEL = "mid level"
SENIOR_LEVEL = "senior level"

SKILL_LEVEL_LIST = [
    (ENTRY_LEVEL, "E"),
    (MID_LEVEL, "M"),
    (SENIOR_LEVEL, "S"),
]


class Tag(models.Model):
    tag = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"{self.tag} {self.pk}"


class SkillLevel(models.Model):
    skill_level = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"{self.skill_level} {self.pk}"


class Job(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    posted_by = models.ForeignKey(Provider, on_delete=models.CASCADE)
    skill_level = models.ForeignKey(
        SkillLevel, on_delete=models.SET_DEFAULT, default=2
    )
    hourly_rate = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    posted = models.DateTimeField(auto_now_add=True)
    location = models.ForeignKey(
        District, on_delete=models.SET_NULL, null=True, blank=True
    )
    postal_code = models.CharField(
        max_length=8, help_text="eg: LC03 101", null=True, blank=True
    )
    tags = models.ManyToManyField(Tag)
    likes = models.BooleanField(default=False)
    dislikes = models.BooleanField(default=False)

    def __str__(self):
        return self.name
