from django.urls import path 
from .import views

urlpatterns = [
    path("signup/",views.sign_up,name='sign_up'),
    path("login/",views.log_in,name='sign_in'),
    path("",views.retrive,name="read"),
    # path("email/",views.send_email,name='send'),
    path("confirm_otp/",views.confirm_otp,name="confirm_otp"),
    path("save/",views.save,name="savewithotp"),
   
]