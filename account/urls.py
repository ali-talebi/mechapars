from .views import Register_View , Login_View , Logout_View , Team_View
from django.urls import path
app_name = 'account'


urlpatterns = [
    path('register/' , Register_View.as_view() , name = "register" ) ,
    path('login/', Login_View.as_view(), name="login"),
    path('logout/' , Logout_View.as_view() , name="logout") ,
    path('Team_View/' , Team_View.as_view() , name ="team" ) ,
    path('Team_View/<int:page>/', Team_View.as_view(), name="team"),

]
