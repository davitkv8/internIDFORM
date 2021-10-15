from django.contrib import admin
from .models import UsersID


class ReadOnlyAdmin(admin.ModelAdmin):
    readonly_fields = ['date_expires', 'mrz']


admin.site.register(UsersID, ReadOnlyAdmin)
