from datetime import datetime

from django.db import models

NULLABLE = {"blank": True, "null": True}


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Наименование",
        help_text="Введите наименование товара",
    )
    description = models.TextField(
        max_length=100,
        verbose_name="Описание",
        help_text="Напишите описание",
        **NULLABLE
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"
        ordering = ("name",)


class Products(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Наименование",
        help_text="Введите наименование товара",
    )
    description = models.TextField(
        verbose_name="Описание", help_text="Напишите описание", **NULLABLE
    )
    image = models.ImageField(
        upload_to="products/",
        verbose_name="Превью",
        help_text="Загрузите картинку",
        **NULLABLE
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="Категория",
        help_text="Укажите категорию",
        **NULLABLE,
        related_name="products"
    )
    price = models.IntegerField(
        verbose_name="Цена за покупку", help_text="Укажите цену товара", **NULLABLE
    )
    date_created_at = models.DateTimeField(
        default=datetime.now,
        verbose_name="Дата добавления",
        help_text="ДД.ММ.ГГГГ",
        **NULLABLE
    )
    date_updated_at = models.DateTimeField(
        default=datetime.now,
        verbose_name="Дата изменения",
        help_text="ДД.ММ.ГГГГ",
        **NULLABLE
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        ordering = (
            "name",
            "category",
            "price",
            "date_created_at",
            "date_updated_at",
        )


class BlogRecord(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name="Заголовок",
        help_text="Введите заголовок",
    )
    slug = models.CharField(
        max_length=100, verbose_name="Ссылка", help_text="Введите ссылку", **NULLABLE
    )
    text = models.TextField(
        verbose_name="Содержание", help_text="Напишите текст", **NULLABLE
    )
    image = models.ImageField(
        upload_to="blog/",
        verbose_name="Превью",
        help_text="Загрузите картинку",
        **NULLABLE
    )
    date_created_at = models.DateTimeField(
        default=datetime.now,
        verbose_name="Дата добавления",
        help_text="ДД.ММ.ГГГГ",
        **NULLABLE
    )
    is_active = models.BooleanField(default=True, verbose_name="Активна")
    count_views = models.PositiveIntegerField(
        default=0,
        verbose_name="Количество просмотров",
        **NULLABLE
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "запись"
        verbose_name_plural = "записи"
        ordering = (
            "title",
            "slug",
            "text",
            "image",
            "date_created_at",
            "is_active",
            "count_views",
        )


class Version(models.Model):
    product = models.ForeignKey(
        Products,
        on_delete=models.CASCADE,
        **NULLABLE,
        verbose_name="продукт"
    )
    number_ver = models.FloatField(
        verbose_name="Номер версии",
        help_text="Укажите номер версии",
        **NULLABLE
    )
    name_ver = models.CharField(
        max_length=100,
        verbose_name="Название версии",
        help_text="Укажите название версии",
    )
    is_active = models.BooleanField(default=True, verbose_name="Активная версия")

    def __str__(self):
        return self.name_ver

    class Meta:
        verbose_name = "Версия"
        verbose_name_plural = "Версии"
        ordering = (
            'number_ver',
            'name_ver',
            'is_active',
            'product',
        )
