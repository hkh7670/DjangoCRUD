from django.shortcuts import render
from .models import Post
from .forms import PostForm
from django.utils import timezone
from django.shortcuts import redirect

# Create your views here.
def index(request):
    posts = Post.objects.all()
    context = {"posts": posts}
    return render(request, "index.html", context)

def create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            # post.title = request.title
            # post.body = request.body
            # post.pub_date = timezone.now()
            post.save()
            return redirect('index')
    else:
        form = PostForm()
    return render(request, "create.html", {"form": form})

def postView(request, id):
    post = Post.objects.get(pk=id)
    context = {"post": post}
    return render(request, "postView.html", context)

def postDelete(request, id):
    post = Post.objects.get(pk=id)
    post.delete()
    return redirect("index")