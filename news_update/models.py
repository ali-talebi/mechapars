from django.db import models

# Create your models here.


class News_Letter(models.Model) :

    email = models.EmailField(verbose_name= 'ایمیل عضویت در خبرنامه'  , unique=True  )

    def __str__(self):
        return self.email


    class Meta :
        db_table = "News_Letter"
        verbose_name_plural = 'اعضای خبرنامه '