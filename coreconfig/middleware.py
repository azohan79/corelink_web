from django.shortcuts import render
from django.utils.deprecation import MiddlewareMixin

from .models import SiteSettings


class DevelopmentModeMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # админку не трогаем
        if request.path.startswith('/admin/'):
            return None

        settings_obj = SiteSettings.get_solo()

        # если режим разработки включён и пользователь не админ
        if settings_obj.development_mode:
            user = request.user
            if not (user.is_authenticated and (user.is_staff or user.is_superuser)):
                # показываем шаблон-заглушку
                return render(request, 'maintenance.html', status=503)

        # иначе пропускаем дальше
        return None
