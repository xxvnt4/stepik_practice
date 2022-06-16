from django import forms
from .models import User

# class UserForm(forms.Form):
#     name = forms.CharField()
#     age = forms.IntegerField()

class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('name', 'age')