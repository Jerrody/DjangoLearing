# Generated by Django 3.1 on 2020-08-20 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='template',
            field=models.CharField(default='blog/home.html', max_length=100, verbose_name='Template'),
        ),
    ]
