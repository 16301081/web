from django.urls import path,include
from . import views
import likes.views as likeviews

urlpatterns = [
    path('me/', views.me,name='me'),
    path('', views.nlogin,name='login'),
    path('logout/', views.nlogout,name='logout'),
    path('register/', views.register,name='register'),
    path('change_psw/',views.change_psw,name='change_psw'),
    path('weibo_add/',views.weibo_add,name='weibo_add'),
    path('like_change/', likeviews.like_change, name='like_change'),
    path('search_info/', views.search_info, name='search_info'),
]