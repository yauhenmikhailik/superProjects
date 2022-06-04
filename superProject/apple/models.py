from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=250, verbose_name="Категория")

    def __str__(self):
        return self.name


class Product(models.Model):
    KINDS = (
        ('Выбор 1', 'Выбор 1'),
        ('Выбор 2', 'Выбор 2'),
    )

    title = models.CharField(max_length=250, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    price = models.DecimalField(max_digits=6,decimal_places=2, verbose_name="Цена")
    image= models.ImageField(upload_to='images', null=True, verbose_name="Изображения")
    created = models.DateTimeField(auto_created=True, verbose_name="Дата")
    update=models.DateTimeField(auto_now=True)
    categories = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name="Категория")
    kind = models.CharField(max_length=7, choices=KINDS, default='Выбор 1' ,verbose_name="Список")


    def __str__(self):
        return self.title


class Shop(models.Model):
    name = models.CharField(max_length = 30, verbose_name="Название")
    citi = models.CharField(max_length = 30, verbose_name="Город")
    street = models.CharField(max_length = 30, verbose_name="Адресс")
    products = models.ManyToManyField('Product')

    def __str__(self):
        return self.name

# Create your models here.
