from django.contrib.auth.models import User
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Menu(models.Model):
    name = models.CharField('Name', max_length=100)
    is_auth = models.BooleanField('Is Authenticated', default=False)
    active = models.BooleanField('Active', default=False)

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
        null=True, blank=True,
        related_name='children'
    )
    menu = models.ForeignKey(
        Menu,
        verbose_name='Menu',
        on_delete=models.CASCADE
    )
    status = models.BooleanField('For Registered', default=False)
    is_auth = models.BooleanField('Is Authenticated', default=False)
    anchor = models.CharField('Anchor', max_length=100)
    url = models.CharField('URL', max_length=100)
    active = models.BooleanField('Active', default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Menu Items'
        verbose_name_plural = 'Menu Items'
