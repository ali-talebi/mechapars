from django.db import models

# Create your models here.
class Company_Information(models.Model) :

    address = models.CharField(verbose_name="آدرس ما" , max_length=200 )
    email1  = models.EmailField(verbose_name= "ایمیل اول ما"  )
    email2  = models.EmailField(verbose_name="ایمیل دوم ما" , blank = True )
    tel1    = models.CharField(max_length=11 , verbose_name="تلفن ۱ ما" )
    tel2    = models.CharField(max_length=11 , verbose_name="تلفن ۲ ما")
    address_map = models.CharField(verbose_name="آدرس ما از روی نقشه " , help_text= "با استفاده از نقشه گوگل مشخصات باید وارد بشود . " , max_length=1000 )
    instagram   = models.CharField(verbose_name="آدرس ما در اینستاگرام" , max_length=200 )
    gmail       = models.CharField(verbose_name="آدرس ایمیل ما" , max_length= 200 )
    telegram    = models.CharField(verbose_name="آدرس ما در تلگرام" , max_length=200 , blank=True   )
    face_book   = models.CharField(verbose_name="آدرس ما در فیسبوک" , max_length=200 , blank = True )
    linkedin    = models.CharField(verbose_name= "آدرس ما در لینکدین" , max_length=200 )



    def __str__(self) :
        return f"آدرس ما * آدرس شرکت "


    class Meta :
        db_table = "Company_Information"
        verbose_name_plural = "مشخصات و اطلاعات ما"



