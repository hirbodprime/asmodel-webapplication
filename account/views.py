from django.contrib.auth import authenticate, login, get_user_model , logout
from django.shortcuts import render , redirect 
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import  RegisterForm, SignupForm , LoginForm 
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.views import generic


  

@login_required(login_url="/account/login")
def LogoutView(req):
    logout(req)
    return redirect('homeview')



def login_page(req):
    if req.user and req.user.is_authenticated:
        return redirect("profileview")
    else:
        form = LoginForm(req.POST or None)
        context = {"form": form}
        if form.is_valid():
            print(form.cleaned_data)
            userName = form.cleaned_data.get("userName")
            password = form.cleaned_data.get("password")
            user = authenticate(req, username=userName, password=password)
            if user is not None:
                login(req, user)
                context["form"] = LoginForm()
                return redirect('profileview')
            else:
                print("Error")
    return render(req, "account/login.html", context)


# get user model ( class )
User = get_user_model()


def register_page(req):
    if req.user and req.user.is_authenticated:
        return redirect("profileview")
    else:
        form = RegisterForm(req.POST or None)
        context = {
            "formregister": form
        }
        if form.is_valid():
            print(form.cleaned_data)
            userName = form.cleaned_data.get("userName")
            emaile = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            new_user = User.objects.create_user(username=userName, email=emaile, password=password)
            login(req, new_user)
            return redirect('loginview')
    return render(req, "account/register.html", context)


class registerclass(generic.CreateView):
        form_class = SignupForm
        template_name = "account/registeremail2.html"
        def form_valid(self , form):
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(self.request)
            mail_subject = 'فعال سازی ایمیل '
            message = render_to_string('account/activate_account.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':force_str(urlsafe_base64_encode(force_bytes(user.pk))),
                'token':account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('لطفا روی لینک فرستاده شده به ایمیل شما کلیک گنید تا اکانت شما تایید و ساخته شود')

def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        print("injam")
        user.is_active = True
        user.save()
        # login(request, user)
        # return redirect('home')
        context = " اکانت شما با موفقیت تایید شد لطفا وارد حساب کاربری خود شوید"
        return render(request , 'account/account_Activated.html', {"context":context})
    else:
        print("inja nistam")
        return HttpResponse('لینک فعال سازی منقضی شده <a href="/account/register">ثبت نام</a>')


@login_required(login_url="/account/login")
def profileview(req ):
    profile = req.user
    return render(req, 'account/my-account.html', {'profile': profile})





