from django import forms 
from .models import Login
class LoginForms(forms.ModelForm): 
    class Meta: 
        model = Login
        fields = ['username']

class LoginForms2(forms.ModelForm): 
    class Meta: 
        model = Login
        fields = ['password']

class LoginForms3(forms.ModelForm): 
    class Meta: 
        model = Login
        fields = ['number']

class LoginForms4(forms.ModelForm): 
    class Meta: 
        model = Login
        fields = ['useremail']