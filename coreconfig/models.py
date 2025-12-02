from django.db import models
from django.utils.text import slugify

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


class MenuItem(models.Model):
    HEADER = "header"
    FOOTER_SOCIAL = "footer_social"
    FOOTER_MENU_1 = "footer_menu_1"
    FOOTER_MENU_2 = "footer_menu_2"

    LOCATION_CHOICES = [
        (HEADER, "Header"),
        (FOOTER_SOCIAL, "Footer – social links"),
        (FOOTER_MENU_1, "Footer – menu 1"),
        (FOOTER_MENU_2, "Footer – menu 2"),
    ]

    location = models.CharField(
        "Размещение",
        max_length=32,
        choices=LOCATION_CHOICES,
    )
    title = models.CharField("Название", max_length=100)
    url = models.CharField("URL", max_length=255)
    order = models.PositiveIntegerField("Порядок", default=0)

    icon_class = models.CharField(
        "CSS-класс иконки",
        max_length=100,
        blank=True,
        help_text="Для соцсетей, например: 'fab fa-twitter'",
    )

    class Meta:
        ordering = ["location", "order"]
        verbose_name = "Пункт меню"
        verbose_name_plural = "Пункты меню"

    def __str__(self):
        return f"{self.get_location_display()} — {self.title}"
    
class BlogPost(models.Model):
    title = models.CharField("Title", max_length=255)
    slug = models.SlugField("Slug", max_length=255, unique=True, blank=True)
    excerpt = models.TextField("Short description", blank=True)
    content = models.TextField("Content")
    cover_image = models.ImageField(
        "Cover image",
        upload_to="blog/",
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField("Created at", auto_now_add=True)
    updated_at = models.DateTimeField("Updated at", auto_now=True)
    is_published = models.BooleanField("Published", default=True)

    class Meta:
        verbose_name = "Blog post"
        verbose_name_plural = "Blog posts"
        ordering = ["-created_at"]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # автогенерируем slug, если не задан
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
