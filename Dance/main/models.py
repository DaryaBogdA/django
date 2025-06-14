from django.db import models


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