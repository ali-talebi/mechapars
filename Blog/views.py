from django.shortcuts import render
from account.models import Personality_Information
from .models import  Post , Category , Tags , Comments_Post
from django.views import View
from .forms import CommentForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.

class Total_Post_View(View) :

    def setup(self, request, *args, **kwargs):
        self.posts = Post.objects.filter(status = 'public' )
        self.categories = Category.objects.all()
        self.total_tags = Tags.objects.all()
        self.top_last_post = Post.objects.filter(status = 'public' ).order_by('-time')[:3]
        return super().setup(request , *args , **kwargs )

    def get(self , request ) :
        return render(request , 'front/blog.html' , {'top_last_post':self.top_last_post , 'tags':self.total_tags , 'categories' : self.categories , 'posts' : self.posts})

    def post(self , request ) :
        return render(request , 'front/blog.html' , { 'top_last_post':self.top_last_post , 'tags':self.total_tags  ,'categories' : self.categories  , 'posts' : self.posts})


class Detail_Post_View(View) :

    def setup(self , request , *args , **kwargs   )  :
        self.select_post = Post.objects.get(id = kwargs['id'])
        self.categories = Category.objects.all()
        self.total_tags = Tags.objects.all()
        self.comment_form = CommentForm
        self.top_last_post = Post.objects.filter(status = 'public' ).order_by('-time')[:3]

        return super().setup(request , *args , **kwargs )

    def get(self , request , id )  :
        form = self.comment_form()
        return render(request , 'front/blog-details.html' , { 'top_last_post':self.top_last_post , 'tags':self.total_tags , 'form' :form , 'categories' : self.categories  , 'post' : self.select_post })
    @method_decorator(login_required(login_url = 'account:login'))
    def post(self , request , id ):
        form = self.comment_form(request.POST)
        if form.is_valid() :
            comment = Comments_Post(post = self.select_post , name = form.cleaned_data['name'] ,
                          email  = form.cleaned_data['email'] ,
                          text = form.cleaned_data['text'] )
            comment.save()
            messages.success(request , 'متن شما با موفقیت ثبت شد' , 'success')

        else :
            messages.error(request , 'مشکلی در ثبت وجود دارد ' , 'error')
        return render(request , 'front/blog-details.html' , { 'top_last_post':self.top_last_post , 'tags':self.total_tags , 'form' : form , 'categories' : self.categories   , 'post' : self.select_post })