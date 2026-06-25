from django import forms
from accounts.models import nUser
from django.contrib.auth.forms import AuthenticationForm

class RegisterForm(forms.ModelForm):
    class Meta:
        model = nUser
        fields = ("username","password", "email", "first_name", "last_name", "phone_n", "address", "profile_p")
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control','placeholder': 'نام کاربری '}),
            'password': forms.TextInput(attrs={'class': 'form-control','placeholder': 'رمز'}),
            'email': forms.EmailInput(attrs={'class': 'form-control','placeholder':'ایمیل'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control','placeholder':'نام'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control','placeholder':'نام خانوادگی'}),
            'phone_n': forms.TextInput(attrs={'class': 'form-control','placeholder':'شماره تلفن همراه با صفر'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3,'placeholder':'آدرس'}),
            'profile_p': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-control modern-input','placeholder': 'نام کاربری خود را وارد کنید','style': 'border-radius: 15px; padding: 12px; transition: all 0.3s;'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control modern-input','placeholder': 'رمز عبور خود را وارد کنید','style': 'border-radius: 15px; padding: 12px; transition: all 0.3s;'}))
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ''