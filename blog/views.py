from django.shortcuts import redirect, render
from .models import BlogModel , ModelComment
from .forms import CommentForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def BlogView(req):
    Blog = BlogModel.objects.all()
    return render(req , 'blog/blog.html',{'blog':Blog})

def BlogDetailView(req , BlogTitle):
    blog = BlogModel.objects.get(BlogTitle = BlogTitle)
    commentobject = ModelComment.objects.filter(accepted = True , motherpost = blog)
    return render(req , 'blog/blog-details.html' , {'b':blog , 'com':commentobject})



@login_required(login_url="/account/login")
def commentView(request , BlogTitle):
    comment = CommentForm(request.POST or None)
    context = {"fc":comment}
    if request.method == "POST":
        if comment.is_valid():
            name = comment.cleaned_data['name']
            email = comment.cleaned_data['email']
            content = comment.cleaned_data['content']
            blog = BlogModel.objects.get(BlogTitle = BlogTitle)
            blogmothere = blog
            comment = ModelComment.objects.create( name = name,email = email , content = content , motherpost = blogmothere )
            if comment.name and comment.email and comment.content != None:
                comment.save()
                return redirect('blogdetailview' ,blog )
    return render(request, 'blog/newcomment.html' , context)
