from django.db import models

# Create your models here.


class Picture_Slider(models.Model) :

    name = models.CharField(verbose_name="اسم تصویر" , max_length=100 )
    picture = models.FileField(verbose_name="تصویر مورد نظر " , upload_to="slider_picture" )
    text    = models.CharField(verbose_name="متن اسلایدر" , max_length=50 , null = True )
    @property
    def return_id(self):
        return self.id

    def __str__(self):
        return f'{self.name}'


    class Meta :
        db_table = "Picture_Slider"
        verbose_name_plural = "تصاویر اسلایدر صفحه اول سایت"

class SELECT_PICTURE_SLIDER(models.Model) :
    obj = models.ForeignKey(Picture_Slider , on_delete=models.CASCADE ,  verbose_name="انتخاب اسلایدر برای نمایش " , help_text="یک اسلایدر برای نمایش در صفحه اول مشخص کنید")

    def __str__(self):
        return f'{self.obj.text}'


    class Meta :
        db_table = "SELECT_PICTURE_SLIDER"
        verbose_name_plural = "انتخاب اسلایدر برای نمایش درصفحه اول"