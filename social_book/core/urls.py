from django.urls import path
from . import views

#path of our website
urlpatterns=[
  path('',views.index,name='index'),#home url,go to view.index
  #''-our own url(if 'profile'-ourwebsite/profile)
  path('settings',views.settings,name='settings'),
  path('profile/<str:pk>',views.profile,name='profile'),
  path('follow',views.follow,name='follow'),
  path('search',views.search,name='search'),
  path('upload',views.upload,name='upload'),
  path('like-post',views.like_post,name='like-post'),
  path('signup',views.signup,name='signup'),
  path('signin',views.signin,name='signin'),
  path('logout',views.logout,name='logout')
  
]