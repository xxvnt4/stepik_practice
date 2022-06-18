from django import forms


class UserForm(forms.Form):
    name = forms.CharField(label='Name', max_length=7, min_length=2, error_messages={
        'max_length': 'Too much symbols!',
        'min_length': 'Too few symbols!',
        'required': 'Enter at least one symbol!'
    })
    age = forms.IntegerField(label='Age')