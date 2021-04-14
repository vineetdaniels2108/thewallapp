from django.db import models
from loginapp.models import *

# Create your models here.

class Message(models.Model):
    user = models.ForeignKey(User, related_name='user_message', on_delete= models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class Comment(models.Model):
    user = models.ForeignKey(User, related_name='user_comment', on_delete = models.CASCADE)
    message = models.ForeignKey(Message, related_name='comment_message', on_delete = models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
    