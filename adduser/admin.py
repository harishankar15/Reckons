from django.contrib import admin
from .models import adduserModel

# Register your models here.


class adduserAdmin(admin.ModelAdmin):
    # list_display = [__all__]
    pass
    

admin.site.register(adduserModel, adduserAdmin)
