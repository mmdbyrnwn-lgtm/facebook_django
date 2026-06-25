from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from django.contrib.auth import login
from django.db import transaction
from core.models import Post
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from core.forms import newpostform

# Create your views here.
def not_user(request):
    return render(request,'core/notuser2.html')
def sey(request):
    if request.user.is_authenticated:
        posts = Post.objects.all().order_by('-created_at')
        return render(request, 'core/index.html', {'posts': posts})
    return redirect('error') 
def p_detail(request,p_id):
    if request.user.is_authenticated:
        post=Post.objects.filter(id=p_id).first()        
        return render(request, 'core/detail.html',context={'posts':post})
    return redirect('error')     
def register(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                messages.success(request, 'ثبت نام با موفقیت انجام شد!')
                return redirect('posts')  
            else:
                for error in form.errors.values():
                    messages.error(request, error)
        else:
            form = UserCreationForm()
    
        return render(request, 'core/register.html', {'form': form})
    return redirect('error') 
def delet_post(request, pk):
    if request.user.is_authenticated:
        post = Post.objects.get(id=pk)
        if post.user != request.user:
            messages.error(request, 'شما اجازه حذف این پست را ندارید!')
            return redirect('posts')
        post.delete()
        messages.success(request,f'پست {post.title} با موفقیت حذف شد')
        return redirect('posts')
    else:
        return redirect('detail', p_id=pk)
def new_post(request):
    if request.user.is_authenticated:
        myform=newpostform()
        if request.method=='POST':
            myform = newpostform(request.POST, request.FILES)
            if myform.is_valid():
                title=myform.cleaned_data['title']
                content=myform.cleaned_data['content']
                image=myform.cleaned_data['image']
                new_post=Post(title=title,content=content,user=request.user,image=image)
                new_post.save()
                messages.success(request,"پست شما با موفقیت ساخته شد")
                return redirect('/posts')
            else :
                print(myform.errors)
                messages.success(request,"پست شما با موفقیت ساخته نشد")

        return render(request,'core/new_post.html',context={'myform':myform})
    return redirect('error') 
def edit_post(request, post_id):
    if request.user.is_authenticated:
        if post.user != request.user:
            messages.error(request, 'شما اجازه ویرایش این پست را ندارید!')
            return redirect('posts')
        post = get_object_or_404(Post, id=post_id)
        if request.method == 'POST':
            form = newpostform(request.POST, request.FILES, instance=post)
            if form.is_valid():
                form.save()
                messages.success(request, 'پست با موفقیت ویرایش شد!')
                return redirect('detail', p_id=post.id)
            else:
                messages.error(request, 'خطا در ویرایش پست')
        else:
            form = newpostform(instance=post)
        return render(request, 'core/edit_post.html', {'form': form, 'post': post})
    return redirect('error') 