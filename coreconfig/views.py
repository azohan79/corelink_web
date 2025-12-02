# coreconfig/views.py

from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.db.models import Q

from .models import BlogPost


def index(request):
    """
    Главная страница CoreLink.
    Шаблон: templates/corelink/index.html
    """
    return render(request, "corelink/index.html")


def about(request):
    """
    Страница About.
    """
    return render(request, "corelink/about.html")


def features_list(request):
    """
    Страница Features (список).
    Пока статичная вёрстка.
    """
    return render(request, "corelink/features.html")


def feature_detail(request, slug=None):
    """
    Детальная страница фичи (пока статичная заглушка).
    """
    return render(request, "corelink/feature_detail.html")


class BlogPostListView(ListView):
    """
    Список постов блога.
    """
    model = BlogPost
    template_name = "corelink/blog_list.html"
    context_object_name = "posts"
    paginate_by = 9

    def get_queryset(self):
        qs = BlogPost.objects.filter(is_published=True).order_by("-created_at")
        q = self.request.GET.get("q")
        if q:
            qs = qs.filter(
                Q(title__icontains=q)
                | Q(excerpt__icontains=q)
                | Q(content__icontains=q)
            )
        return qs


class BlogPostDetailView(DetailView):
    """
    Детальная страница поста блога.
    """
    model = BlogPost
    template_name = "corelink/blog_detail.html"
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["related_posts"] = (
            BlogPost.objects
            .filter(is_published=True)
            .exclude(pk=self.object.pk)
            .order_by("-created_at")[:3]
        )
        return ctx
