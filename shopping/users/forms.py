from django import forms


class LoginFrom(forms.Form):
    username=forms.CharField(required=True)
    password=forms.CharField(required=True,min_length=8)


class RegisterForm(forms.Form):
    user_name=forms.CharField(required=True)
    pwd=forms.CharField(required=True,min_length=8)
    cpwd=forms.CharField(required=True,min_length=8)


class ConsigneeForm(forms.Form):
    name_receive=forms.CharField(required=True)
    address_receive=forms.CharField(required=True)
    zipcode_receive=forms.CharField(required=True,max_length=6)
    mobile_receive=forms.CharField(required=True,max_length=11)