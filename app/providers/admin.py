from re import I
from django.contrib import admin

from .models import Provider, Address, District, Contact, OtherDetails

admin.site.register(Provider)
admin.site.register(Address)
admin.site.register(District)
admin.site.register(Contact)
admin.site.register(OtherDetails)