from django import forms
from .models import News_Letter
from django.core.exceptions import ValidationError

class News_Letter_Form(forms.Form) :

    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control' , 'placeholder' : 'ایمیل'}))

    def clean_email(self):
        new_email = self.cleaned_data['email']
        result = News_Letter.objects.filter(email = new_email ).exists()

        if result :
            raise ValidationError('این ایمیل قبلا در خبر نامه ثبت نام کرده است')

        return new_email
