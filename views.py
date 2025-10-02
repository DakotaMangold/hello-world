from django.shortcuts import render, redirect, get_object_or_404
from .models import Posts
from .forms import PostForm

# Create your views here.
def index(request):
    sentence = "This is the first django view thing"
    return render(request, "index.html", {"sentence": sentence})

def show_post(request):
    post = Posts.objects.all()
    return render(request, "post_list.html", {"post": post})

def add_post(request):
    blogform = PostForm()
    if request.method == "POST":
        blogform = PostForm(request.POST)
        if blogform.is_valid():
            blogform.save()
            return redirect("posts")
    return render(request, "post_form.html", {"blogform": blogform})

def find_post(request, id):
    post = get_object_or_404(Posts, id=id)
    return render(request, "post_detail.html", {"post": post})

def update_post(request, id):
    post = get_object_or_404(Posts, id=id)
    blogform = PostForm(instance=post)
    if request.method == "POST":
        blogform = PostForm(request.POST, instance=post)
        if blogform.is_valid():
            blogform.save()
            return redirect("posts")
    return render(request, "post_form.html", {"blogform": blogform})

def delete_post(request, id):
    post = get_object_or_404(Posts, id=id)
    post.delete()
    return redirect("posts")