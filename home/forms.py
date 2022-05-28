from django import forms
from django.contrib.auth.models import User

class ContactUsForm(forms.Form):
    name = forms.CharField( max_length=100, required=True,label="نام شما (الزامی)",widget=forms.TextInput(attrs={"placeholder":"نام *" }))

    email = forms.EmailField(required=True,label="ایمیل شما (الزامی)",widget=forms.EmailInput(attrs={"placeholder":"ایمیل *"}))

    title = forms.CharField(max_length=300,required=True,label="موضوع",widget=forms.TextInput(attrs={"placeholder":"موضوع *"}))

    content = forms.CharField(max_length=1000,required=True,label="پیام شما",widget=forms.Textarea(attrs={"placeholder":"پیام *", "class":"form-control2"}))
     
    def clean_email(self):
        email = self.cleaned_data.get("email")

        if not "gmail.com" in email:
            raise forms.ValidationError("Email has to be gmail.com")

        return email

