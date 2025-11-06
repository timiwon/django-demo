from django.contrib import admin

from .models import User


# Register your models here.
class CustomerUserAdmin(admin.ModelAdmin):
    #exclude: list[str] = ["password"]
    list_display: list[str] = ["username", "is_staff", "last_login", "date_joined", "is_active"]
    pass

admin.site.register(User, CustomerUserAdmin) 
