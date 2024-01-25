from django.shortcuts import render,HttpResponse,redirect
from .forms import Auth_forms,Confirm_otp
from .models import Auth1
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
import random
otp=random.randint(1000,9999)
print(otp)
def sign_up(request):
    global user
    global form
    if request.method == 'POST':
        form =Auth_forms(request.POST)
        # Auth_forms.get(password=make_password(Auth_forms.password))
        
        if form.is_valid(): 
            user =form.save(commit=False)
            user.password = make_password(user.password)
            aa=user.email
            subject = request.POST.get("subject", "DJANGO_OTP_VERIFICATION:-")
            message = request.POST.get("hello-brother.", str(otp))
            from_email = request.POST.get("from_email", "rkunwardeepsingh@gmail.com")
            to = [str(aa)]
            if subject and message and from_email:
                try:
                    send_mail(subject, message, from_email, to,fail_silently=False)
                    return redirect('confirm_otp')
                except Exception as e:
                    return HttpResponse(f"Invalid header found.{e}")
            else:
                return HttpResponse("Make sure all fields are entered and valid.")
            return redirect("confirm_otp")
        #   return HttpResponse (" registration - successfully:-")
        return HttpResponse("use unique email")
    else:
        form = Auth_forms()
    return render(request, 'sign_up.html', {'form': form})

from django.contrib.auth.decorators import login_required
# from django.utils.decorators import method_decorator

# @method_decorator(login_required,name='dispatch')
def log_in(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        print("login_done")
        return HttpResponse(" log-in ")
        
    else:
        print("else-part")
        return render(request,"log_in.html")
    
# @login_required(login_url='sign_in')
def retrive(request):
    if request.method=="GET":
        v=Auth1.objects.all()
    return render(request,'retrive.html',{'v':v})




# def send_email(request):
#     subject = request.POST.get("subject", "DJANGO_OTP_VERIFICATION:-")
#     message = request.POST.get("message", str(otp))
#     from_email = request.POST.get("from_email", "rkunwardeepsingh@gmail.com")
#     to = ['dip.kapilsolanki@svceindore.ac.in']
#     if subject and message and from_email:
#         try:
#             send_mail(subject, message, from_email, to,fail_silently=False)
#             return HttpResponse("send")
#         except Exception as e:
#             return HttpResponse(f"Invalid header found.{e}")
#         # return HttpResponseRedirect("/contact/thanks/")
#     else:
#         # In reality we'd use a form class
#         # to get proper validation errors.
#         return HttpResponse("Make sure all fields are entered and valid.")
       
def confirm_otp(request):
    if request.method=="POST":
        form=Confirm_otp(request.POST)
        if form.is_valid():
            pwd=form.cleaned_data.get('final_otp')
            if otp==pwd:
                return redirect ("savewithotp")
                # return HttpResponse("valid-otp")
            else:
                return HttpResponse("invalid-otp")
        else:
            return HttpResponse("invalid__form")
    else:
        form=Confirm_otp()
        return render(request,'confirm.html',{'form':form})

def save(request):
    user.save()
    form.save()
    return redirect("read")