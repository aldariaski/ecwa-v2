from django.shortcuts import render, redirect, reverse
from .forms import FormPost, FormComment
from .models import *

def add_post(request):
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
    return render(request,"comment/add_post.html",context)


def detail_post(request, id):
    thepost = Post.objects.get(id=id)
    likes = len(Like.objects.filter(post = thepost))
    comments = Comment.objects.filter(post = thepost)
    context = {
        "post" : thepost,
        "like" : likes,
        "commentlist" : comments,
        "comment_form": FormComment,
        "comment_count": len(comments)
    }
    return render(request, "comment/detail.html", context)

def like_post(request, id):
    if not request.user.is_authenticated:
        return "kontol"
    try:
        like = Like.objects.get(user = request.user, post = Post.objects.get(id=id))
    except:
        like = Like.objects.create(user=request.user, post = Post.objects.get(id=id))
        return redirect(reverse("comment:detail_post", args=[like.post.id]))
    return redirect(reverse("comment:detail_post", args=[id]))

def home(request):
    listofposts = Post.objects.all()
    listofpostandlikes = []
    for posts in listofposts:
        listofpostandlikes.append((posts, len(Like.objects.filter(post = posts))))
    context = {
        "postlist" : listofpostandlikes,
    }
    return render(request, 'comment/listpost.html', context)

def del_com(request, id):
    thecomment = Comment.objects.get(id=id)
    if thecomment.user == request.user:
        thecomment.content = "[deleted]"
        thecomment.deleted = True
        thecomment.save(update_fields=['content', 'deleted'])
    return redirect(reverse("comment:detail_post", args=[thecomment.post.id]))

def del1_com(request, id):
    thecomment = Comment.objects.get(id=id)
    currentpostid = thecomment.post.id
    if request.user.is_superuser:
        thecomment.delete()
    return redirect(reverse("comment:detail_post", args=[currentpostid]))

def comment_post(request, id):
    if not request.user.is_authenticated:
        return "kontol"
    if request.method == "POST":
        comment_form = FormComment(request.POST)
        if comment_form.is_valid():
            comment_form.instance.user = request.user
            comment_form.instance.post = Post.objects.get(id=id)
            comment_form.save()
    return redirect(reverse("comment:detail_post", args=[Post.objects.get(id=id).id]))