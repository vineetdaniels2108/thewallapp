from django.shortcuts import render, redirect, HttpResponse
from .models import *
from loginapp.models import*

# Create your views here.

def wallindex(request):
    logged_user = User.objects.get(id = request.session['user'])
    context = {
        'user' : User.objects.get(id = request.session['user']),
        'all_messages': Message.objects.all(),
        'user_messages': logged_user.user_message.all()
    }
    return render (request, 'wallapp.html', context)

def post_message(request):
    user = User.objects.get(id = request.session['user'])
    message = request.POST['message']
    new_message = Message.objects.create(user = user, message = message)
    return redirect ('/wall')

def post_comment(request):
    user = User.objects.get(id = request.session['user'])
    message = Message.objects.get(id = request.POST['message_id'])
    comment = request.POST['comment']
    new_comment = Comment.objects.create(user = user, message = message, comment = comment)
    return redirect ('/wall')

def delete_comment(request, comment_id): 
    comment = Comment.objects.get(id = comment_id)
    comment.delete()
    return redirect ('/wall')