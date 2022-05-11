from django.contrib import admin
from .models import PersonModel, AddressModel, MovieModel

admin.site.register(PersonModel)
admin.site.register(AddressModel)
admin.site.register(MovieModel)