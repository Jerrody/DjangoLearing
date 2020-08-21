from django.db import models
from django.utils.encoding import iri_to_uri
from django.urls import get_script_prefix


class FeedBackForm(models.Model):
    full_name = models.CharField('Full Name', max_length=100)
    email = models.EmailField('email', max_length=100)
    text = models.CharField('Text FeedBack Form', max_length=200, blank=True)
    slug = models.CharField('slug', max_length=50, unique=True)
    template = models.CharField(
        'Template',
        max_length=100,
        default='pages/feedback_form.html'
    )

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Feedback'
        verbose_name_plural = 'Feedback'

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = ''
        if not f'{self.slug}'.startswith('/'):
            self.slug = '/' + self.slug
        if not self.slug.endswith('/'):
            self.slug += '/'
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return iri_to_uri(get_script_prefix().rstrip('/') + self.slug)

    def get_category_template(self):
        return self.template
