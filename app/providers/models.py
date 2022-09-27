from django.db import models
from django.urls import reverse

class Provider(models.Model):
    title = models.CharField(max_length=6)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_initial = models.CharField(max_length=1)
    
    def get_absolute_url(self):
        return reverse('providers:provider-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return f"{self.title} {self.first_name} {self.middle_initial}. {self.last_name} ({self.pk})"


class District(models.Model):
    district_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.district_name} ({self.pk})"


class Address(models.Model):
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    address1 = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255, blank=True, null=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    postal_code = models.CharField(
        max_length=8,
        help_text="<em><a target='_blank' href='https://stluciapostal.com/postal-codes-2/'>Post Codes</a></em>",
    )

    def __str__(self):
        return f"{self.provider} address"


class Contact(models.Model):
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    tel1 = models.CharField(max_length=50)
    tel2 = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField("alternative email, if any?", blank=True, null=True)

    def __str__(self):
        return f"{self.provider} contact"


class OtherDetails(models.Model):
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    driver_license = models.BooleanField(
        "Do you have a current driving license?", default=False
    )

    def __str__(self):
        return f"{self.provider} ({self.driver_license})"
