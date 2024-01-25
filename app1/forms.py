from django import forms
from .models  import Auth1
class Auth_forms(forms.ModelForm):
  class Meta:
    model=Auth1
    fields=['first_name','last_name','email','password']

 
class Confirm_otp(forms.ModelForm):
  class Meta:
    model=Auth1
    fields=['final_otp']