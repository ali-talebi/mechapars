from django.urls import path
from .views import Service_View
app_name = "service"

urlpatterns = [
    path('services/' , Service_View.as_view() , name = "services" ) ,

]