from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import CreditRequestModel


class UserAdmin(BaseUserAdmin):
    def has_add_permission(self, request, obj=None):
        return False

    list_display_links = None

    list_display = ('user', 'req_date')
    list_filter = ('req_date',)

    search_fields = ()
    ordering = ('-id',)
    filter_horizontal = ()
    readonly_fields = ('user',)


admin.site.register(CreditRequestModel, UserAdmin)
