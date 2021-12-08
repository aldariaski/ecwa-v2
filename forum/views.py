from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout as django_logout
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from django.contrib.auth.models import User
from .models import Post, Like
from comment.forms import FormPost, FormComment
from django.contrib.auth.decorators import login_required

def allthread(request):
    listofposts = Post.objects.all()
    listofpostandlikes = []
    for posts in listofposts:
        listofpostandlikes.append((posts, len(Like.objects.filter(post = posts))))
    context = {
        "postlist" : listofpostandlikes,
    }
    return render(request, 'forum/allthread.html', context)

@login_required(login_url="/account/login")
def newthread(request):
    if not request.user.is_authenticated:
        return "kontol"
    if request.method == "POST":
        post_form = FormPost(request.POST)
        if post_form.is_valid():
            post_form.instance.user = request.user
            post_object = post_form.save()
        return redirect(reverse("comment:detail_post", args=[post_object.id]))

    context = {
        "post_form" : FormPost,
        "is_add_post" : True,
    }
    return render(request, 'forum/newthread.html', context)

@login_required(login_url="/account/login")
def like_post(request, id):
    if not request.user.is_authenticated:
        return "kontol"
    try:
        like = Like.objects.get(user = request.user, post = Post.objects.get(id=id))
        like.delete()
        return redirect(reverse("comment:detail_post", args=[like.post.id]))
    except:
        like = Like.objects.create(user=request.user, post = Post.objects.get(id=id))
        return redirect(reverse("comment:detail_post", args=[like.post.id]))
    return redirect(reverse("comment:detail_post", args=[id]))

@login_required(login_url="/account/login")
def delete_post(request, id):
    postan = Post.objects.get(id=id)
    if request.user.is_superuser or request.user == postan.user:
        postan.delete()
    return redirect("forum:allthread")

@login_required(login_url="/account/login")
def update_post(request):
    if request.method == 'POST':
        postan = Post.objects.get(id = request.POST["idz"])
        poster = request.user.username
        postan.title = request.POST["title"]
        postan.content = request.POST["content"]
        postan.save()
        return redirect('forum:allthread')
    return render(request, 'forum/updatethread.html')