from django.shortcuts import render , redirect
from .models import  Personality_Information , My_Team
from django.contrib.auth.models import  User
from django.views import View
from .forms import Login_Form , Register_Form
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages
from django.contrib.auth.mixins import  LoginRequiredMixin
from news_update.models import News_Letter
from news_update.forms import News_Letter_Form
from django.core.paginator import  Paginator , EmptyPage, PageNotAnInteger
# Create your views here.


class Register_View(View) :


    def dispatch(self, request, *args, **kwargs):
        self.form_reg = Register_Form
        if request.user.is_authenticated :
            return redirect('home:home' )
        return super().dispatch(request , *args , **kwargs )



    def get(self , request ) :

        return render(request , 'front/my-account.html' , {'form_reg' : self.form_reg() })


    def post(self , request ) :
        form_register = self.form_reg(request.POST)




        if form_register.is_valid() :
            new_username = form_register.cleaned_data['username']
            new_email    = form_register.cleaned_data['email']
            new_password = form_register.cleaned_data['password']
            new_person = User.objects.create_user(username = new_username , email=new_email , password=new_password )
            new_person.save()
            new_member = Personality_Information(person = new_person )

            new_member.save( )

            messages.success(request , 'ثبت نام شما با موفقیت انجام شد ' , 'success' )
            return redirect('home:home' )


        else :
            return render(request, 'front/my-account.html', {'form_reg': self.form_reg() })




class Login_View(View) :


    def setup(self, request, *args, **kwargs):
        self.next = request.GET.get("next")
        return super().setup(request , *args , **kwargs )

    def dispatch(self, request, *args, **kwargs):
        self.form_log = Login_Form
        if request.user.is_authenticated :
            return redirect('home:home' )
        return super().dispatch(request , *args , **kwargs )

    def get(self , request ) :

        return render(request , 'front/login_page.html' , {'form_log' : self.form_log()})

    def post(self , request ) :
        form_login    = self.form_log(request.POST)
        if form_login.is_valid() :
            new_username = form_login.cleaned_data['username']
            new_password = form_login.cleaned_data['password']
            user = authenticate(request , username = new_username , password = new_password )

            if user :
                login(request , user )

                messages.success(request , 'با موفقیت وارد شدید' , 'success' )
                if self.next :
                    messages.success(request , 'ابتدا باید وارد حساب کاربری خود شوید' , 'success')
                    return redirect(self.next)
                return redirect('home:home')
            elif user is None :
                messages.error(request , 'در وارد شدن با خطایی روبه روی هستید' , 'error' )


        return render(request , 'front/login_page.html' , {'form_log' : self.form_log()})


class Logout_View(LoginRequiredMixin , View) :
    def get(self , request ):
        logout(request)
        messages.success(request ,  'با موفقیت خارج شدید' , extra_tags='success')
        return redirect('home:home')


    def post(self , request ):
        logout(request)
        messages.success(request ,  'با موفقیت خارج شدید' , extra_tags='success')

        return redirect('home:home')



class Team_View(View) :

    template_name = "front/team.html"

    def setup(self, request, *args, **kwargs):
        self.form = News_Letter_Form


        return super().setup(request , *args , **kwargs )


    def get(self , request , page = 1 ) :
        try :
            total_member  = My_Team.objects.all()
            paginator     = Paginator(total_member , 2 )

            self.my_team  = paginator.page(page)
        except PageNotAnInteger :
            self.my_team  = paginator.page(1)
        except EmptyPage :
            self.my_team  = paginator.page(paginator.num_pages )

        return render(request , self.template_name , { 'form':self.form , 'team' : self.my_team } )

    def post(self , request , page = 1 ) :

        try :
            total_member  = My_Team.objects.all()
            paginator     = Paginator(total_member , 2 )

            self.my_team  = paginator.page(page)
        except PageNotAnInteger :
            self.my_team  = paginator.page(1)
        except EmptyPage :
            self.my_team  = paginator.page(paginator.num_pages )

        form = self.form(request.POST)
        if form.is_valid():
            instance = News_Letter(email = form.cleaned_data['email'] )
            instance.save()
            messages.success(request , 'با موفقیت ثبت شد'  , 'success' )
            return redirect('account:team')

        else :
            messages.success(request , 'قبلا انگار ثبت نام کرده بودی' , 'success')
            return render(request , self.template_name , { 'form':self.form  , 'team' : self.my_team } )
