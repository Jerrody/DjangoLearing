from django.db import models

class Category(models.Model):
    """Model Category"""
    name = models.CharField('name_category', max_length=100)
    slug = models.SlugField('url', max_length=100)


    def __str__(self):
        return self.name

    class Meta():
        verbose_name = 'Category'
        verbose_name_plural = 'Category'