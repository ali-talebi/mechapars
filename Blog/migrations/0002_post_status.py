# Generated by Django 4.2.11 on 2024-03-15 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('public', 'منتشر بشود :)'), ('draft', 'منتشر نشود :(')], max_length=20, null=True, verbose_name='وضعیت انتشار چگونه باشد ؟ '),
        ),
    ]
