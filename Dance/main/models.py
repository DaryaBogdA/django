from django.db import models
from django.contrib.auth.models import User


class Style(models.Model):
    name = models.CharField(max_length=50)
    text = models.TextField()

    class Meta:
        verbose_name_plural = "Стили"

    def __str__(self):
        return self.name

class Teacher(models.Model):
    all_name = models.CharField(max_length=255)
    directions = models.TextField()
    about = models.TextField()

    class Meta:
        verbose_name_plural = "Преподаватели"

    def __str__(self):
        return self.all_name

class Price(models.Model):
    name = models.CharField(max_length=50)
    summa = models.CharField(max_length=7)

    class Meta:
        verbose_name_plural = "Абонементы"

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    username = models.CharField(max_length=32, verbose_name='Имя пользователя')
    last_name = models.CharField(max_length=32, verbose_name='Фамилия')
    surname = models.CharField(max_length=32, verbose_name='Отчество')
    phone = models.CharField(max_length=15, verbose_name='Телефон')

    class Meta:
        verbose_name_plural = "Профили"

    def __str__(self):
        return self.username

