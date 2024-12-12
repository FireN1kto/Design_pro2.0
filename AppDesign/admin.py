from django.contrib import admin
from .models import AdvUser

class AdvUserAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'username','login', 'email')

    readonly_fields = ('username', 'login', 'full_name', 'date_joined')

admin.site.register(AdvUser, AdvUserAdmin)