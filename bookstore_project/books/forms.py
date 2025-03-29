from django import forms
from .models import Book, CustomUser, Profile
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from captcha.fields import CaptchaField


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'price', 'language']


class RegisterForm(UserCreationForm):
    ROLE_CHOICES = [
        ('user', 'Обычный пользователь'),
        ('admin', 'Администратор'),
    ]

    captcha = CaptchaField()
    role = forms.ChoiceField(choices=ROLE_CHOICES, required=True, label="Роль")

    class Meta:
        model = CustomUser
        fields = ("username", "email", "password1", "password2", "role", 'captcha')

    def save(self, commit=True):
        user = super().save(commit=False)

        if self.cleaned_data["role"] == "admin":
            user.is_staff = True
            user.is_superuser = True
        else:
            user.is_staff = False
            user.is_superuser = False

        if commit:
            user.save()
        return user


class ProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ["username", "email", "phone_number"]


class ProfileExtraForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio']


class BookFilterForm(forms.Form):
    SORT_CHOICES = [
        ("title_asc", "Название (А-Я)"),
        ("title_desc", "Название (Я-А)"),
        ("price_asc", "Цена (по возрастанию)"),
        ("price_desc", "Цена (по убыванию)"),
    ]

    sort_by = forms.ChoiceField(label="Сортировка", choices=SORT_CHOICES, required=False)
