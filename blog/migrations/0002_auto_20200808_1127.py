# Generated by Django 3.0.8 on 2020-08-08 08:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.TextField(blank=True, default='', max_length=100, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='category',
            name='paginated',
            field=models.PositiveIntegerField(default=5, verbose_name='Count Post in Page'),
        ),
        migrations.AddField(
            model_name='category',
            name='published',
            field=models.BooleanField(default=True, verbose_name='Display'),
        ),
        migrations.AddField(
            model_name='category',
            name='sort',
            field=models.PositiveIntegerField(default=0, verbose_name='Order'),
        ),
        migrations.AddField(
            model_name='category',
            name='template',
            field=models.CharField(default='blog/post_list.html', max_length=500, verbose_name='Template'),
        ),
        migrations.AddField(
            model_name='post',
            name='edit_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Edit Date'),
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='post/', verbose_name='Main Image'),
        ),
        migrations.AddField(
            model_name='post',
            name='published',
            field=models.BooleanField(default=True, verbose_name='Publish'),
        ),
        migrations.AddField(
            model_name='post',
            name='published_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Publish Date'),
        ),
        migrations.AddField(
            model_name='post',
            name='sort',
            field=models.PositiveIntegerField(default=0, verbose_name='Order'),
        ),
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.BooleanField(default=False, verbose_name='For Registered'),
        ),
        migrations.AddField(
            model_name='post',
            name='template',
            field=models.CharField(default='blog/post_detail.html', max_length=500, verbose_name='Template'),
        ),
        migrations.AddField(
            model_name='tag',
            name='published',
            field=models.BooleanField(default=True, verbose_name='Display or Not?'),
        ),
    ]
