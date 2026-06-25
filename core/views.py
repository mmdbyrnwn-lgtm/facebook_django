from django.shortcuts import render,redirect,get_object_or_404
from core.models import Post
from django.contrib import messages
from core.forms import newpostform


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
        return render(request,'core/new_post.html',context={'myform':myform})
    return redirect('error') 


def edit_post(request, post_id):
    if request.user.is_authenticated:
        post = get_object_or_404(Post, id=post_id)
        if post.user != request.user:
            messages.error(request, 'شما اجازه ویرایش این پست را ندارید!')
            return redirect('posts')
        post = get_object_or_404(Post, id=post_id)
        if request.method == 'POST':
            form = newpostform(request.POST, request.FILES, instance=post)
            if form.is_valid():
                form.save()
                messages(request, 'پست با موفقیت ویرایش شد!')
                return redirect('detail', p_id=post.id)
        return render(request, 'core/edit_post.html', {'form': form, 'post': post})
    return redirect('error') 