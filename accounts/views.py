from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .forms import RegisterForm, LoginForm  # ✅ اسم درست رو import کن
from django.contrib.auth.hashers import make_password

def register_view(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            user.password = make_password(request.POST.get('password'))
            user.save()
            login(request, user)
            messages.success(request, f'ثبت نام موفق! {user.username} خوش آمدید 🎉')
            return redirect('posts')
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})



def login_view(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'خوش آمدید {username} 🤗')
                return redirect('posts')
    return render(request, 'accounts/login.html', {'form': form})


 
def logout_view(request):
    logout(request)
    messages.success(request, 'با موفقیت خارج شدید! 👋')
    return redirect('login')
