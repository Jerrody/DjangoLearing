from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Page(models.Model):
    title = models.CharField('Title', max_length=100)
    text = models.TextField('Text', max_length=500)
    active = models.BooleanField('Active', default=True)
    template = models.CharField(
        'Template',
        max_length=100,
        default='page/index.html'
    )
    slug = models.SlugField('slug', max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Page'
        verbose_name_plural = 'Page'

    def get_absolute_url(self):
        return reverse('page_detail', kwargs={'slug': self.slug})

    def get_category_template(self):
        return self.template
