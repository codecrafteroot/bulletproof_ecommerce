# thirdparty imports
from uuid import uuid4
from hashlib import md5

# builtin imports
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.html import mark_safe

# local imports
from ..managers import UserManager


class UserModel(AbstractUser):
    uuid = models.UUIDField(default=uuid4, unique=True)
    email = models.EmailField(_("email address"), unique=True)
    about_me = models.TextField(_("About me"), null=True, blank=True)
    is_costumer = models.BooleanField('Costumer status', default=True)
    is_signup_completed = models.BooleanField('Signup status', default=False)

    picture = models.ImageField(_("user picture"), upload_to='images/user/picture/', default='defaults/user_default.png')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    objects = UserManager()

    class Meta:
        db_table = "users"
        ordering = ("uuid",)
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __repr__(self):
        return self.uuid

    def __unicode__(self):
        return self.email

    def __str__(self):
        # Override the default __str__ of AbstractUser that returns username, which may
        # lead to leaking sensitive data in logs.
        return self.username
    
    def picture_preview(self): #new
        return mark_safe('<img src = "{url}" width = "50"/>'.format(
             url = self.picture.url
        ))
    
    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(
            digest, size)