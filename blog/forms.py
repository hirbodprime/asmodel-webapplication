from django import forms

class CommentForm(forms.Form):

    name = forms.CharField( max_length=100,label="نام شما (الزامی)",widget=forms.TextInput(attrs={"placeholder":"نام *" }))
    
    email = forms.EmailField(label="ایمیل شما (الزامی)",widget=forms.EmailInput(attrs={"placeholder":"ایمیل *"}))

    content = forms.CharField(max_length=1000,label=" پیام شما (الزامی)",widget=forms.Textarea(attrs={"placeholder":"پیام *"}))
     
    def clean_email(self):
        email = self.cleaned_data.get("email")

        if not "gmail.com" in email:
            raise forms.ValidationError("Email has to be gmail.com")

        return email