from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email обязателен")
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("role", "admin")
        return self.create_user(username, email, password, **extra_fields)


class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ("user", "Обычный пользователь"),
        ("admin", "Администратор"),
    ]

    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default="user")  # Поле роли

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    published_date = models.DateField(null=True, blank=True)
    isbn = models.CharField(max_length=20, unique=True, null=True, blank=True)
    pages = models.IntegerField(null=True, blank=True)
    cover = models.CharField(max_length=255, null=True, blank=True)
    language = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.title
