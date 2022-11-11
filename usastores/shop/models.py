from django.db import models
from django.urls import reverse


class Category(models.Model):
    """Класс Category"""
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        """Класс Meta класса Category"""
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        """Возвращает название категории"""
        return self.name

    def get_absolute_url(self):
        """Формирует ссылку по заданному шаблону"""
        return reverse('shop:product_list_by_category',
                       args=[self.slug])


class Product(models.Model):
    """Класс Product"""
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, verbose_name='Категория')
    name = models.CharField(max_length=200, db_index=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, db_index=True, verbose_name='URL')
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, verbose_name='Фото')
    description = models.TextField(blank=True, verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    stock = models.PositiveIntegerField(verbose_name='Количество')
    available = models.BooleanField(default=True, verbose_name='Наличие')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    class Meta:
        """Класс Meta класса Product"""
        ordering = ('name',)
        index_together = (('id', 'slug'),)
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        """Возвращает название категории"""
        return self.name

    def get_absolute_url(self):
        """Формирует ссылку по заданному шаблону"""
        return reverse('shop:product_detail',
                       args=[self.id, self.slug])
