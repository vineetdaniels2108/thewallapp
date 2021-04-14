from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.wallindex),
    path('/post_message', views.post_message), 
    path('/post_comment', views.post_comment),
    path('/delete/<int:comment_id>', views.delete_comment)
]