from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from .managers import UserManager


class User(AbstractBaseUser):
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=12, unique=True)
    full_name = models.CharField(max_length=250)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    avatar = models.ImageField(upload_to='media', null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['email', 'full_name']

    def __str__(self):
        return f"{self.full_name} --- {self.is_active}"

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_active


class OtpCode(models.Model):
    phone_number = models.CharField(max_length=11, unique=True)
    code = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.phone_number} - {self.code} - {self.created}'


class OtpCodeForgot(models.Model):
    email = models.EmailField()
    code = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.email} - {self.code} - {self.created}'
