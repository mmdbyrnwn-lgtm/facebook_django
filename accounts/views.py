from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .forms import RegisterForm, LoginForm
from django.urls import reverse

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(request.POST.get('password'))  # ← بهتر از make_password
            user.save()
            
            login(request, user)
            messages.success(request, f'ثبت نام موفق! {user.username} خوش آمدید 🎉')
            return redirect('core:posts')
        # اگر فرم نامعتبر بود، به قالب برگرد با خطاها
    else:
        form = RegisterForm()
    
    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                messages.success(request, f'خوش آمدید {username} 🤗')
                
                next_url = request.GET.get('next')
                return redirect(next_url) if next_url else redirect('core:posts')
            
            messages.error(request, 'نام کاربری یا رمز عبور اشتباه است!')
        else:
            messages.error(request, 'لطفاً اطلاعات را صحیح وارد کنید.')
            messages.error(request, 'نام کاربری یا رمز عبور اشتباه است!')
    else:
        form = LoginForm()
    
    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.success(request, 'با موفقیت خارج شدید! 👋')
    return redirect('accounts:login')