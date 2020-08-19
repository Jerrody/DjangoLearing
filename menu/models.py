from django.contrib.auth.models import User
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Menu(models.Model):
    name = models.CharField('Name', max_length=100)
    is_auth = models.BooleanField('Is Authenticated', default=True)
    active = models.BooleanField('Active', default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menu'


class MenuItems(MPTTModel):
    name = models.CharField('Name', max_length=50)
    title = models.CharField('Name Post', max_length=100)
    parent = TreeForeignKey(
        'self',
        verbose_name='Parent Menu',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children'
    )
    menu = models.ForeignKey(
        Menu,
        verbose_name='Menu',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    status = models.BooleanField('For Registered', default=True)
    is_auth = models.BooleanField('Is Authenticated', default=True)
    anchor = models.CharField('Anchor', max_length=100)
    url = models.URLField('URL', max_length=100)
    active = models.BooleanField('Active', default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Menu Items'
        verbose_name_plural = 'Menu Items'
