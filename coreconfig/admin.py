from django.contrib import admin
from .models import SiteSettings, MenuItem, BlogPost

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ('development_mode', 'updated_at')
    readonly_fields = ('updated_at',)

    def has_add_permission(self, request):
        # запрещаем создавать больше одной записи
        if SiteSettings.objects.exists():
            return False
        return super().has_add_permission(request)
    

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ("title", "location", "url", "order")
    list_filter = ("location",)
    search_fields = ("title", "url")
    ordering = ("location", "order")
    
@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title", "is_published", "created_at")
    list_filter = ("is_published", "created_at")
    search_fields = ("title", "excerpt", "content")
    prepopulated_fields = {"slug": ("title",)}

