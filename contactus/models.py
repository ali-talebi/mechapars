from django.db import models
from django_jalali.db import models as jmodels
# Create your models here.


class Contact_US(models.Model) :
    STATUS_CHOICE = (
        ('un_do' , 'عدم رسیدگی' ) ,
        ('in_do' , 'در حال رسیدگی') ,
        ('out_do' , 'تمام شده')
    )
    name  = models.CharField(verbose_name="نام کاربری" , max_length=100 )
    email = models.EmailField(verbose_name="ایمیل " )
    phone = models.CharField(verbose_name="شماره تلفن" , max_length=11 )
    subject = models.CharField(verbose_name="موضوع " , max_length= 50 )
    text    = models.TextField(verbose_name= "متن ارسال شده" )
    time    = jmodels.jDateTimeField(verbose_name = "تاریخ ارسال" , auto_now_add = True )
    status  = models.CharField(verbose_name="وضعیت رسیدگی به تیکت" , max_length=20 , choices=STATUS_CHOICE , default='un_do')

    def __str__(self):
        return self.name

    class Meta :
        db_table = "Contact_US"
        verbose_name_plural = "تیکت های ارتباط با ما"