from django.urls import path
from core.views import sey,p_detail,new_post,not_user,delet_post,edit_post
from . import views

app_name = 'core'   # ← این خط رو اضافه کنید

urlpatterns = [
    path('',sey,name='posts' ),
    path('detail/<int:p_id>/',p_detail,name='detail' ),
    path('new/post/',new_post,name='new_post' ),
    path('error/',not_user, name='error'),
    path('post/<int:pk>/delete/', delet_post, name='delete'),
    path('edit/<int:post_id>/',edit_post, name='edit_post'),
    path('post/<int:post_id>/like/', views.toggle_like, name='toggle_like'),
]