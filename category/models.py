from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=20, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(max_length=250)
    category_imgae = models.ImageField(upload_to='photos/categories', blank=True)

    class Meta:
        verbose_name_plural = 'Categories'
        
    def __str__(self):
        return self.category_name
