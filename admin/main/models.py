from django.utils.translation import gettext_lazy as _

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.hashers import (
    check_password,
    is_password_usable,
    make_password,
)
from django.utils.crypto import salted_hmac

class CustomUser(AbstractUser):
    """Админ"""

    class Meta:
        db_table = "admin_user"
        verbose_name = _("Пользователь")
        verbose_name_plural = _("Пользователи")




# Create your models here.
class SiteUser(models.Model):
    first_name = None
    last_login = None
    is_staff = None
    date_joined = None
    name = models.CharField(_("first name"), max_length=150, blank=True)
    email = models.EmailField(_("email address"), unique=True)
    # hashed_password = models.CharField(_("hashed_password"), max_length=128)
    password = models.CharField(_("password"), max_length=128, db_column="hashed_password")

    def __str__(self):
        return self.email
    #
    # def set_password(self, raw_password):
    #     self.hashed_password = make_password(raw_password)
    #     self.password = make_password(raw_password)
    #     self._password = raw_password
    #
    # def check_password(self, raw_password):
    #     """
    #     Return a boolean of whether the raw_password was correct. Handles
    #     hashing formats behind the scenes.
    #     """
    #
    #     def setter(raw_password):
    #         self.set_password(raw_password)
    #         # Password hash upgrades shouldn't be considered password changes.
    #         self._password = None
    #         self.save(update_fields=["hashed_password"])
    #     return check_password(raw_password, self.hashed_password, setter)
    #
    # def set_unusable_password(self):
    #     # Set a value that will never be a valid hash
    #     self.hashed_password = make_password(None)
    #
    # def has_usable_password(self):
    #     """
    #     Return False if set_unusable_password() has been called for this user.
    #     """
    #     return is_password_usable(self.hashed_password)
    #
    # def get_session_auth_hash(self):
    #     """
    #     Return an HMAC of the password field.
    #     """
    #     key_salt = "django.contrib.auth.models.AbstractBaseUser.get_session_auth_hash"
    #     return salted_hmac(
    #         key_salt,
    #         self.password,
    #         algorithm="sha256",
    #     ).hexdigest()

    class Meta:
        managed = False
        db_table = "user"
        verbose_name = "Пользователь сайта"
        verbose_name_plural = "Пользователи сайта"
