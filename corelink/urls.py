from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import BlogPostListView, BlogPostDetailView

from coreconfig import views

app_name = "corelink"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path('features/', views.features, name='features'),
    path('feature-detail/', views.feature_detail, name='feature_detail'),
    path("blog/", BlogPostListView.as_view(), name="blog_list"),
    path("blog/<slug:slug>/", BlogPostDetailView.as_view(), name="blog_detail"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
