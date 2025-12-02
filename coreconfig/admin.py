from django.contrib import admin
from .models import SiteSettings

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ('development_mode', 'updated_at')
    readonly_fields = ('updated_at',)

    def has_add_permission(self, request):
        # запрещаем создавать больше одной записи
        if SiteSettings.objects.exists():
            return False
        return super().has_add_permission(request)

