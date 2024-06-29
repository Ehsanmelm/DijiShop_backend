from django.contrib import admin
from .models import SellerModel , StoreModel , StuffModel

# Register your models here.

admin.site.register(SellerModel)
admin.site.register(StoreModel)
admin.site.register(StuffModel)