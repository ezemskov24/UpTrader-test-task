from django.db import models


class Menu(models.Model):
    """
    Модель Меню

    name - Название меню
    parent - Родительский элемент меню.
    url - URL для ссылки меню.
    named_url - Именованный URL для ссылки меню
    """

    name = models.CharField(max_length=100)
    parent = models.ForeignKey(
        'self',
        related_name='children',
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )
    url = models.CharField(max_length=100, blank=True)
    named_url = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name
