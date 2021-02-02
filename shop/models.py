from django.db import models
from django.urls import reverse

class Product(models.Model):
    slug = models.SlugField() # Для создание своих URL
    title = models.CharField(max_length=120)
    description = models.TextField()
    img = models.ImageField(default='default.png', upload_to='goods_img')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('shop_detail', kwargs={'slug': self.slug})