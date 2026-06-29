from django import forms
from django.contrib.auth.models import User
from core.models import Post
class newpostform(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content','image']
        labels = {'title': 'عنوان پست','content': 'محتوا','image': 'تصویر',}
        widgets = {'title': forms.TextInput(attrs={'class': 'form-control','placeholder': 'عنوان پست را وارد کنید'}),
                   'content': forms.Textarea(attrs={'class': 'form-control','rows': 8,'placeholder': 'متن پست خود را بنویسید...'}),
                   'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),}


