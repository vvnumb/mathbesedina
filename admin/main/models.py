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
    hashed_password = models.CharField(_("password"), max_length=127,
                                       db_column="hashed_password", blank=True, default="")

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
        return f"Ученик {full_name}"

    class Meta:
        managed = False
        db_table = "user"
        verbose_name = "Пользователь сайта"
        verbose_name_plural = "Пользователи сайта"


class Textbook(models.Model):
    """Учебник"""
    school_class = models.IntegerField()
    title = models.CharField(_("Название"), max_length=127)
    slug = models.CharField(_("Название в ссылке"), max_length=127, unique=True)
    
    def __str__(self):
        return f"Учебник {self.title}"

    class Meta:
        managed = False
        db_table = "textbook"
        verbose_name = "Учебник"
        verbose_name_plural = "Учебники"


class Video(models.Model):
    title = models.CharField(_("Название видео"), max_length=127)
    link = models.CharField(_("Ссылка на видео в источнике"), max_length=127)
    
    def __str__(self):
        return f"Видео {self.title}"
    
    class Meta:
        managed = False
        db_table = "video"
        verbose_name = "Видео"
        verbose_name_plural = "Видео"


class Topic(models.Model):
    """Тема урока"""
    textbook = models.ForeignKey(Textbook, on_delete=models.SET_NULL, blank=True, null=True)
    title = models.CharField(_("Название"), max_length=127)
    description = models.CharField(_("Описание"), max_length=256)
    slug = models.CharField(_("Название в ссылке"), max_length=127, blank=True, null=True)
    
    videos = models.ManyToManyField(
        to="Video",
        through="VideoXTopic",
        through_fields=("topic", "video"),
        blank=True
    )
    tests = models.ManyToManyField(
        to="Test",
        through="TestXTopic",
        through_fields=("topic", "test"),
        blank=True
    )
    
    def __str__(self):
        return f"Тема {self.textbook.title}| {self.title}"
    
    class Meta:
        managed = False
        db_table = "topic"
        verbose_name = "Тема урока"
        verbose_name_plural = "Темы урока"


class Test(models.Model):
    title = models.CharField(_("Название"), max_length=127)
    description = models.CharField(_("Описание"), max_length=256)
    slug = models.CharField(_("Название в ссылке"), max_length=127, unique=True, blank=True,
                            null=True)
    school_class = models.IntegerField()
    
    topics = models.ManyToManyField(
        to="Topic",
        through="TestXTopic",
        through_fields=("test", "topic"),
        blank=True
    )
    
    def __str__(self):
        return f"Тест|{self.school_class}| {self.title}"
    
    class Meta:
        managed = False
        db_table = "test"
        verbose_name = "Тест"
        verbose_name_plural = "Тесты"


class VideoXTopic(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    
    class Meta:
        managed = False
        db_table = "video_x_topic"
        auto_created = True


class TestXTopic(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    
    class Meta:
        managed = False
        db_table = "test_x_topic"
        auto_created = True
