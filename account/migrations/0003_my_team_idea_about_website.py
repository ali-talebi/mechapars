# Generated by Django 4.2.11 on 2024-03-16 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_my_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='my_team',
            name='idea_about_website',
            field=models.CharField(help_text='نظر شما در وبسیات منتشر خواهد شد', max_length=300, null=True, verbose_name='نظر  شما در مورد وبسایت'),
        ),
    ]
