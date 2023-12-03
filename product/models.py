from django.db import models
from django.utils.text import slugify
from django.urls import reverse


class Category(models.Model):
    category_name = models.CharField(max_length=250)
    category_slug = models.SlugField(max_length=250, allow_unicode=True)
    image = models.ImageField(upload_to='category-images')

    def __str__(self):
        return self.category_name
    
    def save(self, *args, **kwargs):
        self.category_slug = slugify(self.category_name, allow_unicode=True)
        return super().save(*args, **kwargs)
    

class Product(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, allow_unicode=True)
    mojod = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    old_price = models.IntegerField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='product-images')
    status = models.BooleanField(default=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        return super().save(*args, **kwargs)
    
    @property
    def get_detail_url(self):
        return reverse('product:product-detail', args=[self.slug])
    