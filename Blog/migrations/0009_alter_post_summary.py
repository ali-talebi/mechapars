# Generated by Django 4.2.11 on 2024-03-18 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0008_post_summary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='summary',
            field=models.CharField(help_text='لطفا به طوری مروری نوشته شود', max_length=50, null=True, verbose_name='خلاصه متن مروری در 30 کلمه'),
        ),
    ]
