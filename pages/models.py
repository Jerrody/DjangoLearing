from django.db import models
from django.urls import get_script_prefix
from django.utils.encoding import iri_to_uri
from django.utils.translation import gettext_lazy as _
from django.urls import reverse


class Page(models.Model):
    """Pages"""
    title = models.CharField('Title', max_length=100)
    sub_title = models.CharField(
        'Sub Title',
        max_length=500,
        blank=True,
        null=True
    )
    text = models.TextField('Text', max_length=500)
    active = models.BooleanField('Active', default=True)
    edit_date = models.DateTimeField(
        'Date Editing',
        auto_now=True,
        blank=True,
        null=True
    )
    published_date = models.DateTimeField(
        'Data Publishing',
        blank=True,
        null=True
    )
    published = models.BooleanField('Publish?', default=True)
    template = models.CharField(
        'Template',
        max_length=100,
        default='blog/home.html'
    )
    registration_required = models.BooleanField(
        'Need to be a Sigh Up',
        help_text='Only registered users can view this page',
        default=True
    )
    slug = models.SlugField('slug', max_length=50, unique=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = ''
        if not f'{self.slug}'.startswith('/'):
            self.slug = '/' + self.slug
        if not self.slug.endswith('/'):
            self.slug += '/'
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Page'
        verbose_name_plural = 'Page'

    def get_absolute_url(self):
        return reverse('page_detail', kwargs={'slug': self.slug})

    def get_category_template(self):
        return self.template
