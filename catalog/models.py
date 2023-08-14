from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='id')
    name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.TextField(max_length=1000, verbose_name='Описание')
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100,
                              verbose_name='Изображение', **NULLABLE)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    price = models.IntegerField(verbose_name='Цена')
    date_creation = models.DateTimeField(max_length=150, verbose_name='Дата создания')
    date_change = models.DateTimeField (max_length=150, verbose_name='Дата изменения')

    def __str__(self):
        return f'''
        {self.name}, {self.description},
        Категория: {self.category}
        Цена: {self.price}
        '''

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.TextField(max_length=1000, verbose_name='Описание')

    def __str__(self):
        return f'{self.name} {self.description}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
