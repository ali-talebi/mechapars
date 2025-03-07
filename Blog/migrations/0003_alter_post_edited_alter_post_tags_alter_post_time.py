# Generated by Django 4.2.11 on 2024-03-15 20:50

from django.db import migrations, models
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0002_post_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='edited',
            field=django_jalali.db.models.jDateTimeField(auto_now=True, verbose_name='زمان ویرایش'),
        ),
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(help_text='از قسمت تگ های مقالات ُ این فیلد مقدار دهی میشود', to='Blog.tags', verbose_name='تگ های مقالات'),
        ),
        migrations.AlterField(
            model_name='post',
            name='time',
            field=django_jalali.db.models.jDateTimeField(auto_now_add=True, verbose_name='زمان ساخت'),
        ),
    ]
