from django.shortcuts import render , redirect
from .models import Contact_US
from .forms import Contact_Us_Form
from .models import Contact_US
from  django.views import View
from django.contrib import messages
from aboutus.models import Company_Information
# Create your views here.

class Contact_Us_View(View) :

    template_name = "front/contact.html"

    def setup(self, request, *args, **kwargs):
        self.form = Contact_Us_Form
        self.informations = Company_Information.objects.first()
        return super().setup(request , *args , **kwargs )

    def get(self , request ) :
        return render(request , self.template_name , {'information' : self.informations , 'form':self.form})

    def post(self , request ) :
        form = self.form(request.POST)
        if form.is_valid() :
            form.save()
            messages.success(request , 'با موفقیت ثبت شد')
            return redirect('contactus:contactus')
        else :
            messages.error(request , 'در ارتباط شما مشکلی ایجاد شده است')
            return render(request , self.template_name , { 'information' : self.informations  , 'form':self.form})

    