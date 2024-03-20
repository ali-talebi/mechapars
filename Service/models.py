from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.


class Service_Information(models.Model) :

    name      = models.CharField(verbose_name= "اسم خدمت" , max_length=100 )
    picture   = models.FileField(verbose_name='تصویر خدمت' , upload_to='service_picture/' )
    picture2  = models.FileField(verbose_name="تصویر خدمت ۲" , upload_to='service_picture/' , null = True )
    introduce = models.CharField(verbose_name="معرفی نامه خدمت" , max_length= 100 , null=True )
    text      = RichTextField(verbose_name="متن توضیحات" )


    def __str__(self):
        return self.name

    class Meta :
        db_table = "Service_Information"
        verbose_name_plural = "خدمات شرکت مکا "

