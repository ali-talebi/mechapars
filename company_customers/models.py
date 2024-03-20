from django.db import models

# Create your models here.


class Companies(models.Model) :

    name = models.CharField(verbose_name="نام حقوقی شرکت"  , max_length= 100 )
    picture = models.FileField(verbose_name="لوگوی شرکت" , upload_to="Company_Customers_picture"  )



    def __str__(self):
        return self.name

    class Meta :
        db_table = "Companies"
        verbose_name_plural = "مشتریان سازمانی مکا"