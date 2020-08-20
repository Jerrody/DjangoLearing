from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.sites.models import Site
from django.db import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Menu(models.Model):
    """Menu"""
    name = models.CharField('Name', max_length=100)
    is_auth = models.BooleanField('Is Authenticated', default=True)
    published = models.BooleanField('Publish?', default=True)

    def __str__(self):
        return self.name

    def items(self):
        return self.menuitem_set.all()

    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menu'


class MenuItems(MPTTModel):
    """Menu Elements"""
    name = models.CharField('Name', max_length=50)
    title = models.CharField('Name Menu Attribute', max_length=100)
    parent = TreeForeignKey(
        'self',
        verbose_name='Parent Menu',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children'
    )
    menu = models.ForeignKey(
        'Menu',
        verbose_name='Menu',
        on_delete=models.CASCADE,
    )
    status = models.BooleanField('For Registered', default=False)
    anchor = models.CharField('Anchor', max_length=100,  null=True, blank=True)
    url = models.URLField('URL', max_length=100,  null=True, blank=True)

    content_type = models.ForeignKey(
        ContentType,
        verbose_name='URL on',
        # limit_choices_to=settings.MENU_APPS,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    object_id = models.PositiveIntegerField(
        'ID Recording',
        default=1,
        null=True
    )
    content_object = GenericForeignKey('content_type', 'object_id')
    sort = models.PositiveIntegerField('Order', default=0)
    published = models.BooleanField('Publish?', default=True)

    def get_anchor(self):
        if self.anchor:
            return "{}/#{}".format(
                Site.objects.get_current().domain,
                self.anchor
            )
        else:
            return False

    def __str__(self):
        return self.name

    content_object.short_description = 'ID'

    class Meta:
        verbose_name = 'Menu Items'
        verbose_name_plural = 'Menu Items'

    class MPTTMeta:
        order_insertion_by = ('sort',)
