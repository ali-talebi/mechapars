from django.shortcuts import render , redirect
from django.views import View
from Service.models import Service_Information
from Blog.models import Post
from account.models import My_Team
from news_update.models import News_Letter
from news_update.forms import News_Letter_Form
from django.contrib import messages
from .models import SELECT_PICTURE_SLIDER
from company_customers.models import Companies
from projects.models import Project_information
# Create your views here.


class Home(View) : 

	def setup(self, request, *args, **kwargs):
		self.company_customers = Companies.objects.all()
		self.form_news_register = News_Letter_Form
		self.team = My_Team.objects.all()
		self.top_post  = Post.objects.all()[:3]
		self.top_posts_one = Post.objects.all().order_by('-time' )[:1]
		self.services = Service_Information.objects.all()
		self.picture_slider   =  SELECT_PICTURE_SLIDER.objects.first()
		self.projects = Project_information.objects.all()
		return super().setup(request , *args , **kwargs )

	def get(self , request ) : 
		return render(request , 'front/index-2.html' , {
			'projects' : self.projects ,
			'company_customers' : self.company_customers ,
			'picture_slider':self.picture_slider ,'form' :self.form_news_register  , 'team' : self.team , 'top_posts_one':self.top_posts_one , 'top_posts':self.top_post , 'services' : self.services})


	def post(self , request ) :
		news_letter = self.form_news_register(request.POST)
		if news_letter.is_valid() :
			new_email = News_Letter(email=news_letter.cleaned_data['email'])
			new_email.save()
			messages.success(request, 'با موفقیت ثبت نام در خبرنامه انجام شد', 'success')

		else :

			messages.success(request , 'انگار قبلا ثبت نام کرده بودی'  , 'success' )

		return render(request , 'front/index-2.html', {
			'projects' : self.projects ,
			'company_customers': self.company_customers,
			'picture_slider':self.picture_slider ,'form':self.form_news_register  , 'team' : self.team , 'top_posts_one':self.top_posts_one  , 'top_posts':self.top_post  , 'services' : self.services})



