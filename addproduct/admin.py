from django.contrib import admin
from .models import addproductModel

# Register your models here.


class addproductAdmin(admin.ModelAdmin):
    #list_display = []
    pass
    

admin.site.register(addproductModel, addproductAdmin)
