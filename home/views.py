from django.shortcuts import render , redirect
from shop.models import productmodel , categories
from .forms import ContactUsForm 
from .models import ModelContact 
from blog.models import BlogModel
# Create your views here.
def homeview(req):
    cate = categories.objects.filter(pk__in=[4,2,1])
    cate1 = categories.objects.filter(pk__in=[3,5])
    cate2 = categories.objects.filter(pk__in=[6,9,2])
    cate3 = categories.objects.filter(pk__in=[1,2,3,4,5,6,8,9,10,11])
    pro = productmodel.objects.filter(categoryMain=1 , firstpage=True, deleted=False)
    pro1 = productmodel.objects.filter(categoryMain=2,firstpage=True , deleted=False)
    blog = BlogModel.objects.filter(vip=True)
    return render(req , 'home/index.html' , 
        {
        'cate':cate ,
        'cate1':cate1,
        'pr':pro,
        'pr1':pro1,
        'cate2':cate2,
        'cate3':cate3,
        'bloge':blog
        }
    )


def contactview(request):
    contact = ContactUsForm(request.POST or None)
    context = {"form": contact}
    if request.method == "POST":
            if contact.is_valid():
                name = contact.cleaned_data['name']
                email = contact.cleaned_data['email']
                title = contact.cleaned_data['title']
                content = contact.cleaned_data['content']
                contact = ModelContact.objects.create(name = name  , email = email ,title = title , content = content )
                contact.save()
                return redirect('HomeView')
    return render(request, 'Home/contact.html' , context)



def coming(req):
    return render(req , 'Home/Others/coming-soon.html')
def faq(req):
    return render(req , 'Home/Others/faq.html')
def privacy(req):
    return render(req , 'Home/Others/privacy-policy.html')
def h404(req):
    return render(req , 'Home/HttpErrors/404.html')
def aboutview(req):
    return render(req , 'Home/about.html')