from django.contrib import admin
from .models import AdvUser,InteriorDesignRequest,Category

class AdvUserAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'username', 'email', 'status')

    readonly_fields = ( 'username', 'first_name', 'last_name', 'full_name', 'date_joined')

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ('email',)
        return self.readonly_fields


class InterDesignRequestAdmin(admin.ModelAdmin):
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)

        if obj and obj.status in ['В процессе', 'Завершена']:
            form.base_fields['status'].disabled = True

        return form

class RequestInline(admin.TabularInline):
    model = InteriorDesignRequest
    extra = 0

class CategoryAdmin(admin.ModelAdmin):
    inlines = [RequestInline]

admin.site.register(AdvUser, AdvUserAdmin)
admin.site.register(InteriorDesignRequest, InterDesignRequestAdmin)
admin.site.register(Category, CategoryAdmin)