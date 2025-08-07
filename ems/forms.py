from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Record


from django.forms.widgets import PasswordInput, TextInput

from django import forms

# create user

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

# login 

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())

# Create a record

class CreateRecordForm(forms.ModelForm):

    class Meta:
        model = Record
        fields = '__all__'


# Update a record

class UpdateRecordForm(forms.ModelForm):

    class Meta:
        model = Record
        fields = '__all__'


# Search a record
class SearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100)

"""# Department filter
class DepartmentFilterForm(forms.Form):
    department = forms.CharField(label='Department Name', max_length=100, required=False)"""