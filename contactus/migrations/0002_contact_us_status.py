# Generated by Django 4.2.11 on 2024-03-18 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactus', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact_us',
            name='status',
            field=models.CharField(choices=[('un_do', 'عدم رسیدگی'), ('in_do', 'در حال رسیدگی'), ('out_do', 'تمام شده')], default='un_do', max_length=20, verbose_name='وضعیت رسیدگی به تیکت'),
        ),
    ]
