from django.shortcuts import render
from .models import Post
from .forms import PostForm
from django.utils import timezone
from django.shortcuts import redirect, get_object_or_404


# Create your views here.
def postList(request):
    title = request.GET.get('title', '')
    body = request.GET.get('body', '')
    posts = Post.objects.filter(title__icontains=title, body__icontains=body).order_by("-pub_date")
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
