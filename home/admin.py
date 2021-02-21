from django.contrib import admin
from .models import Contact
from .models import ContactInformation, Testomonials,Servicesinfo
# Register your models here.
admin.site.register(Contact)
admin.site.register(ContactInformation)
admin.site.register(Testomonials)
admin.site.register(Servicesinfo)
