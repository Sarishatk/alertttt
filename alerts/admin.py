from django.contrib import admin
from .models import Alert

@admin.register(Alert)
class AlertAdmin(admin.ModelAdmin):
    list_display = ("date", "alert_name", "tower", "status", "entered_by", "last_updated_by", "updated_at")
    list_filter = ("status", "tower", "date")
    search_fields = ("alert_name", "update", "entered_by", "last_updated_by")
    readonly_fields = ("created_at", "updated_at")
