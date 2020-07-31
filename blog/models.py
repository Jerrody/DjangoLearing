from django.db import models


class Category(models.Model):
    """Model Category"""
    name = models.CharField('Name', max_length=100)
    slug = models.SlugField('Slug', max_length=50)

    def __str__(self):
        return self.name

    class Meta():
        verbose_name = 'Category'
        verbose_name_plural = 'Category'


class Tag(models.Model):
    """Model Tag"""
    name = models.CharField('Name', max_length=100)
    slug = models.SlugField('Slug', max_length=50)

    def __str__(self):
        return self.name

    class Meta():
        verbose_name = 'Tag'
        verbose_name_plural = 'Tag'


class Post(models.Model):
    """Model Post"""
    title = models.CharField('Name Post', max_length=100)
    mini_text = models.TextField('Text Post', max_length=500)
    text = models.TextField('Mini Text', max_length=1000)
    created_date = models.DateTimeField('Date Time', auto_now=True, auto_now_add=False)
    slug = models.SlugField('Slug', max_length=50)

    def __str__(self):
        return self.title

    class Meta():
        verbose_name = 'Post'
        verbose_name_plural = 'Post'


class Comment(models.Model):
    """Model Comment"""
    text = models.TextField('Text', max_length=100)
    created_date = models.DateTimeField('Date Time', max_length=100)
    moderation = models.BooleanField()

    def __str__(self):
        return self.text

    class Meta():
        verbose_name = 'Comment'
        verbose_name_plural = 'Comment'
