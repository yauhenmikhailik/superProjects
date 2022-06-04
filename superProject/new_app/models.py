from django.db import models



class Person(models.Model):
    nik_name = models.CharField(max_length=30, verbose_name="Имя профиля")
    login = models.CharField(max_length=20, verbose_name="Логин", unique=True)
    password = models.CharField(max_length=30, verbose_name="Пароль")
    avatar = models.ImageField(upload_to='images', null=True, verbose_name="Фото профиля")

    def __str__(self):
        return self.nik_name


class A(models.Model):
    name = models.CharField(max_length=30, verbose_name="Имя профиля")
    age = models.PositiveIntegerField