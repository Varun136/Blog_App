from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns=[
    path('',blogList.as_view(),name='bloglist'),
    path('login/',customLoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(next_page='bloglist'),name='logout'),
    path('register/',registerView.as_view(),name='register'),
    path('blog-details/<int:pk>',blogDetails.as_view(),name='blogdetails'),
    path('create-blog/',blogCreate.as_view(),name='create-blog'),
    path('update/<int:pk>',blogUpdate.as_view(),name='blogUpdate'),
    path('delete/<int:pk>',blogDelete.as_view(),name='blogDelete'),
    path('myblogs',myBlogs.as_view(),name='myblogs'),
    path('category/<int:pk>',getCategoryDetails,name='categories'),
    path('comments/<int:pk>',getComments,name='comments')
]