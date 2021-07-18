from django.contrib import admin
from .models import WaitlistEntry

class WaitlistEntryAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'notes', 'created_at')
    search_fields = ('first_name',)

admin.site.register(WaitlistEntry, WaitlistEntryAdmin)