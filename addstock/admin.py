from django.contrib import admin
from .models import addstockModel

# Register your models here.


class addstockAdmin(admin.ModelAdmin):
    # list_display = [__all__]
    pass
    

admin.site.register(addstockModel, addstockAdmin)
