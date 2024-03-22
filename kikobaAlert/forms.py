from django import forms

from .models import Customer

# This is Registartion Form Model for Customer with all necessary fields
# such as firstName , lastName , emailAddress , phoneNumber , password
class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

# Here is Login Form Model for Customer with all necessary fields for login
# such as emailAddress and password

class LoginForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['email', 'password']        
        