from django.contrib import admin
from django.urls import path
from coreconfig import views

app_name = "corelink"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIR)
