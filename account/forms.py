from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class LoginForm(forms.Form):
    userName = forms.CharField(label="نام کاربری",
        widget=forms.TextInput(attrs={"class": "account_form login", "placeholder": "نام کاربری خود را وارد کنید"})
    )
    password = forms.CharField(label="رمز",
        widget=forms.PasswordInput(attrs={"class": "account_form login", "placeholder": "رمز خود را وارد کنید"})
    )

    def clean_userName(self):
        userName = self.cleaned_data.get("userName")
        qs = User.objects.filter(username=userName)
        if not qs.exists():
            raise forms.ValidationError("نام کاربری  یا رمز اشتباه است")
        return userName

    def clean_pass(self):
        passwoRd = self.cleaned_data.get("password")
        if not User.objects.filter(password=passwoRd):
            raise forms.ValidationError("نام کاربری  یا رمز اشتباه است")
        return passwoRd
        
        

class RegisterForm(forms.Form):
    
    error_css_class = 'text-danger'
    required_css_class = 'required'
    userName = forms.CharField(label="نام کاربری ",
        widget=forms.TextInput(attrs={"class": "account_form register", "placeholder": "نام کاربری مورد نظر را وارد کنید"})
    )

    email = forms.EmailField(label=" ایمیل",
        widget=forms.EmailInput(attrs={"class": "account_form register", "placeholder": "ایمیل خود را وارد کنید"})
    )

    password = forms.CharField(label=" رمز",
        widget=forms.PasswordInput(attrs={"class": "account_form register", "placeholder": "رمز عبور"})
    )

    password2 = forms.CharField(
        label="تکرار رمز",
        widget=forms.PasswordInput(attrs={"class": "account_form register", "placeholder": "تکرار رمز عبور"})
    )
    
    def clean_userName(self):
        # User = get_user_model()
        userName = self.cleaned_data.get("userName")
        qs = User.objects.filter(username=userName)
        if qs.exists():
            raise forms.ValidationError("نام کاربری قبلا استفاده شده است")
        return userName

    def clean_email(self):
        
        email = self.cleaned_data.get("email")
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("ایمیل از قبل وجود دارد")
        return email

    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        if password != password2:
            raise forms.ValidationError("پسورد ها یکی نیست")
        return data



from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200)
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')





#  class ReceiverForm(forms.ModelForm):
#      phone_number = forms.RegexField(regex=r'^\+?1?\d{9,15}$',
#                                      error_message = ("Phone number must be entered in the format: '+999999999'. Up to 15 digits is allowed."))
#     phone = PhoneNumberField(label="شماره تماس")