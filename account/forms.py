from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class Register_Form(forms.Form) :

    username = forms.CharField(widget=forms.TextInput())
    email    = forms.EmailField()
    password = forms.CharField( widget=forms.PasswordInput())



    def clean_username(self):
        new_username  = self.cleaned_data['username']
        user = User.objects.filter(username =  new_username ).exists()
        if user :
            raise ValidationError('نام کاربری قبلا انتخاب شده است')

        return new_username


    def clean_email(self):
        new_email = self.cleaned_data['email']
        email = User.objects.filter(email = new_email).exists()
        if email :
            raise ValidationError('این ایمیل قبلا ثبت نام کرده است')

        return new_email


    def clean_password(self):
        new_password = self.cleaned_data['password']
        if len(new_password) < 8 :
            raise ValidationError('رمز ایمیل شما باید حداقل 8 کاراکتر باشد')

        return new_password



class Login_Form(forms.Form) :

    username = forms.CharField( widget=forms.TextInput())
    password = forms.CharField( widget=forms.PasswordInput())

