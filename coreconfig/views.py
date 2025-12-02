from django.shortcuts import render


def index(request):
    """
    Главная страница CoreLink.
    Шаблон: templates/corelink/index.html
    """
    return render(request, "corelink/index.html")

def about(request):
    return render(request, "corelink/about.html")


def features(request):
    return render(request, "corelink/features.html")


def feature_detail(request):
    return render(request, "corelink/feature_detail.html")


