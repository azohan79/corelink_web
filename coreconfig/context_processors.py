from .models import MenuItem


def corelink_menus(request):
    return {
        "header_menu": MenuItem.objects.filter(
            location=MenuItem.HEADER
        ).order_by("order"),
        "footer_social_menu": MenuItem.objects.filter(
            location=MenuItem.FOOTER_SOCIAL
        ).order_by("order"),
        "footer_menu_1": MenuItem.objects.filter(
            location=MenuItem.FOOTER_MENU_1
        ).order_by("order"),
        "footer_menu_2": MenuItem.objects.filter(
            location=MenuItem.FOOTER_MENU_2
        ).order_by("order"),
    }