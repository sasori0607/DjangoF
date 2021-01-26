from django.db import models
from django.contrib.auth.models import User

class News(models.Model):
    title = models.CharField("Name", max_length=100)
    text = models.TextField("Основной текст")
    avtor = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
    def __str__(self):
        return self.title