from django.db import models
from django.urls import reverse





class Category(models.Model):
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=120, verbose_name='Название категории')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        reverse('shop_category', kwargs={'slug': self.category.slug})




class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery')
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='images')


class Product(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=120)
    prise = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='цена')
    category = models.ForeignKey('Category', verbose_name='Выбор категории', on_delete=models.CASCADE, default=None)
    description = models.TextField()
    img = models.ImageField(default='default.png', upload_to='goods_img')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('shop_detail', kwargs={'slug': self.slug, 'category': self.category.slug})

