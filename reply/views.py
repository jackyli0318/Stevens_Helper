from django.shortcuts import render, HttpResponse
from django import forms
from .models import Reply
from blocks.models import Block
from posts.models import Post
from users.models import User
import json

# Create your views here.


def create_reply(request):

    # reply_obj = json.loads(params)
    # reply_obj = request.POST['params']
    post_id = int(request.POST.get('post_id'))
    content = request.POST.get('content')
    email = request.session.get('email')

    post = Post.objects.get(id=post_id)
    user = User.objects.get(email=email)

    if content != '':
        reply = Reply(content=content)
        reply.post = post
        reply.author = user
        reply.author_name = user.nickname
        reply.status = 1
        reply.save()

        status = 'ok'
        error = ''

    else:
        status = 'fail'
        error = 'Please input content.'

    reply_obj = {
        'status': status, 'error': error
    }
    # print (reply_obj)
    # return json.dumps(reply_obj)
    # return request, reply_obj
    return HttpResponse(json.dumps(reply_obj), content_type='application/json')


def reply_detail(post_id):
    post_id = int(post_id)
    reply_objs = Reply.objects.filter(post=post_id).order_by('update_timestamp')
    return reply_objs