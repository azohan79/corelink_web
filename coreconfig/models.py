from django.db import models

# Create your models here.
class SiteSettings(models.Model):
    development_mode = models.BooleanField(
        default=True,
        verbose_name="Режим разработки включён",
        help_text="Если включено — все пользователи видят заглушку, "
                  "админы и staff видят реальный сайт."
    )

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Настройки сайта"
        verbose_name_plural = "Настройки сайта"

    def __str__(self):
        return "Глобальные настройки"

    @classmethod
    def get_solo(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj
