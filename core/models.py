from django.db import models
from accounts.models import nUser
# Create your models here.

class Post(models.Model):
    title=models.CharField(max_length=200)
    content =models.CharField(max_length=1024)
    user=models.ForeignKey(nUser,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    update_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'{self.title} : {self.user.username}'

class Comment(models.Model):
    user =models.ForeignKey(nUser,on_delete=models.CASCADE)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    body=models.CharField(max_length=1024)
    def __str__(s):
        return f'{s.user.username}'