from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    """Model Category"""
    name = models.CharField('Name', max_length=100)
    slug = models.SlugField('Slug', max_length=50)
    description = models.TextField(
        'Description',
        max_length=100,
        default='',
        blank=True
    )
    parent = TreeForeignKey(
        'self',
        verbose_name='Parent Category',
        on_delete=models.CASCADE,
        null=True, blank=True,
        related_name='children'
    )
    template = models.CharField(
        'Template',
        max_length=500,
        default='blog/post_list.html'
    )
    published = models.BooleanField('Display', default=True)
    paginated = models.PositiveIntegerField('Count Post in Page', default=5)
    sort = models.PositiveIntegerField('Order', default=0)

    def __str__(self):
        return self.name

    class Meta():
        verbose_name = 'Category'
        verbose_name_plural = 'Category'

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_slug': self.slug})


class Tag(models.Model):
    """Model Tag"""
    name = models.CharField('Name', max_length=100)
    slug = models.SlugField('Slug', max_length=50)
    published = models.BooleanField('Display or Not?', default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tag'


class Post(models.Model):
    """Model Post"""
    author = models.ForeignKey(
        User,
        verbose_name='Author',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    title = models.CharField('Name Post', max_length=100)
    mini_text = models.TextField('Text Post', max_length=500)
    text = models.TextField('Mini Text', max_length=1000)
    created_date = models.DateTimeField(
        'Date Time',
        auto_now=True,
        auto_now_add=False
    )
    slug = models.SlugField('Slug', max_length=50)
    edit_date = models.DateTimeField(
        'Edit Date',
        default=timezone.now,
        blank=True,
        null=True
    )
    published_date = models.DateTimeField(
        'Publish Date',
        default=timezone.now,
        blank=True,
        null=True
    )
    image = models.ImageField(
        'Main Image',
        upload_to='post/',
        blank=True,
        null=True
    )
    category = models.ForeignKey(
        Category,
        verbose_name = 'Category',
        on_delete=models.CASCADE,
        null=True
    )
    tags = models.ManyToManyField(
        Tag,
        verbose_name='Tag',
        blank=True,
        related_name='tag'
    )
    template = models.CharField(
        'Template',
        max_length=500,
        default='blog/post_detail.html'
    )
    published = models.BooleanField('Publish', default=True)
    status = models.BooleanField('For Registered', default=False)
    sort = models.PositiveIntegerField('Order', default=0)
    viewed = models.PositiveIntegerField('Viewed', default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name='Post'
        verbose_name_plural = 'Post'

    def get_category_template(self):
        return self.category.template

    def get_absolute_url(self):
        return reverse(
            'post_detail',
            kwargs={'category': self.category.slug,
            'slug': self.slug}
        )

    def get_tags(self):
        return self.tags.all()

    def get_comcounts(self):
        return self.comments.count()


class Comment(models.Model):
    """Model Comment"""
    author = models.ForeignKey(
        User,
        verbose_name='Author',
        on_delete=models.CASCADE
    )
    text = models.TextField('Text', max_length=100)
    created_date = models.DateTimeField('Date Time', max_length=100, auto_now=True)
    moderation = models.BooleanField(default=True)
    post = models.ForeignKey(
        Post,
        verbose_name='Post',
        on_delete=models.CASCADE,
        related_name='comments'
    )

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comment'
