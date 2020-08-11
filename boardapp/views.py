from django.shortcuts import render
from .models import Post
from .forms import PostForm
from django.utils import timezone
from django.shortcuts import redirect, get_object_or_404
import logging
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.core import serializers
import json


logger = logging.getLogger(__name__)

# Create your views here.
def postList(request):
    # logger.info("request : {}".format(request))
    print(dict(request.GET))
    print("title : ", request.GET.get('title', ''))
    print("body : ", request.GET.get('body', ''))
    title = request.GET.get('title', '')
    body = request.GET.get('body', '')
    posts = Post.objects.filter(title__icontains=title, body__icontains=body).order_by("-pub_date")
    # posts = Post.objects.filter(Q(title__icontains=title) | Q(body__icontains=title)).order_by("-pub_date")
    print("Post Query :", posts.query, "\n")
    # posts = Post.objects.all().order_by("-pub_date")
    context = {"posts": posts}
    return render(request, "postList.html", context)


def postCreate(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            # post.title = request.title
            # post.body = request.body
            # post.pub_date = timezone.now()
            post.save()
            return redirect("postList")
    else:
        form = PostForm()
    return render(request, "postCreate.html", {"form": form})


def postView(request, id):
    post = Post.objects.get(pk=id)
    context = {"post": post}
    return render(request, "postView.html", context)


def postDelete(request, id):
    post = Post.objects.get(pk=id)
    post.delete()
    return redirect("postList")


def postUpdate(request, id):
    post = get_object_or_404(Post, pk=id)

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            # post.title = request.title
            # post.body = request.body
            # post.pub_date = timezone.now()
            post.save()
            return redirect("postList")
    else:
        form = PostForm(instance=post)
    return render(request, "postUpdate.html", {"form": form})

def apiTest(request):
    if(request.method == "GET"):
        # JsonResponse 사용
        # posts = list(Post.objects.values())
        # return JsonResponse(posts, safe=False)

        # HttpResponse 사용
        posts = Post.objects.all()
        postsJson = serializers.serialize('json', posts)
        return HttpResponse(postsJson, content_type="application/json")
