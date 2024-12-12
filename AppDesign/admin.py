from django.contrib import admin
from .models import AdvUser

class AdvUserAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'username', 'email')

    readonly_fields = ( 'username', 'first_name', 'last_name', 'full_name', 'date_joined')

admin.site.register(AdvUser, AdvUserAdmin)