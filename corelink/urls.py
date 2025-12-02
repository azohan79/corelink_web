from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from coreconfig import views as core_views

urlpatterns = [
    path("admin/", admin.site.urls),

    # основные страницы
    path("", core_views.index, name="index"),
    path("about/", core_views.about, name="about"),

    # features (список + деталка)
    path('features/', views.features, name='features'),
    path('feature-detail/', views.feature_detail, name='feature_detail'),

    # блог (список + деталка)
    path("blog/", core_views.BlogPostListView.as_view(), name="blog_list"),
    path("blog/<slug:slug>/", core_views.BlogPostDetailView.as_view(), name="blog_detail"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
