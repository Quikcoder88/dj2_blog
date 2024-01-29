from django.db import models
from django.contrib.auth import get_user_model  # берем стандартную модель юзера

User = get_user_model()  # создаем класс юзера


class Category(models.Model):
    """Класс категорий"""
    title = models.CharField("Название", max_length=50)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.title


class Tag(models.Model):
    """Класс тегов статей"""
    title = models.CharField("Тэг", max_length=50)

    class Meta:
        verbose_name = "Тэг"
        verbose_name_plural = "Тэги"

    def __str__(self):
        return self.title


class News(models.Model):
    """Класс новостей"""
    user = models.ForeignKey(  # автор статьи
        User,
        verbose_name="Автор",
        on_delete=models.CASCADE)  # при удалении юзера удаляем все его статьи

    category = models.ForeignKey(  # категория статьи
        Category,
        verbose_name="Категория",
        on_delete=models.SET_NULL,  # при удалении категории поле устанавливается в NULL
        null=True)  # категория в статье может отсутствовать

    title = models.CharField("Заголовок", max_length=100)  # Заголовок статьи
    text_min = models.TextField("Превью", max_length=350)  # превью статьи
    text = models.TextField("Текст статьи")  # полный текст статьи
    tags = models.ManyToManyField(Tag, verbose_name="Тэги")  # У одной статьи
    created = models.DateTimeField("Дата создания", auto_now_add=True)  # дата создания статьи
    description = models.CharField("Описание", max_length=100)
    keywords = models.CharField("Ключевые слова", max_length=50)

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"

    def __str__(self):
        return self.title

