from django.utils.translation import gettext_lazy as _

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.timezone import now


class CustomUser(AbstractUser):
    """Админ"""

    class Meta:
        db_table = "admin_user"
        verbose_name = _("Пользователь")
        verbose_name_plural = _("Пользователи")


class SiteUser(models.Model):
    """Пользователь сайта"""
    name = models.CharField(_("Имя"), max_length=127, blank=True)
    middle_name = models.CharField(_("Отчество"), max_length=127, blank=True)
    last_name = models.CharField(_("Фамилия"), max_length=127, blank=True)
    birth_date = models.DateField(_("день рождения"))

    email = models.EmailField(_("почта"), unique=True)
    username = models.CharField(_("никнейм"), max_length=127, unique=True)
    password = models.CharField(_("password"), max_length=127, db_column="hashed_password", blank=True, default="")

    is_active = models.BooleanField(_("Активен"), default=True)
    is_superuser = models.BooleanField(_("Админ"), default=False)
    is_subscribed = models.BooleanField(_("Подписан"), default=False)

    created_at = models.DateTimeField(_("создан в"), default=now)
    updated_at = models.DateTimeField(_("обновлен в"), default=now)
    subscription_ends = models.DateTimeField(_("окончание подписки"), blank=True)
    last_login_at = models.DateTimeField(_("последний раз заходил"), blank=True)

    def __str__(self):
        full_name = f"{self.last_name} {self.name}"
        if self.middle_name:
            full_name += f" {self.middle_name}"
        return full_name

    class Meta:
        managed = False
        db_table = "user"
        verbose_name = "Пользователь сайта"
        verbose_name_plural = "Пользователи сайта"
