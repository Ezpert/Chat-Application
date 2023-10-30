from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


class MyUserManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError('Users must have a username')

        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user


class UserProfile(AbstractBaseUser):
    username = models.CharField(max_length=255, unique=True, default='None')
    password = models.CharField(max_length=128, default='')

    objects = MyUserManager()

    USERNAME_FIELD = 'username'
