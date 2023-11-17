from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post, Comment
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.decorators import login_required





def index(request):
    posts_list = Post.objects.order_by("-pub_date")[:5]
    context = {
        "posts_list": posts_list,
    }
    return render(request, "blog/index.html", context)


def detail(request, post_id):
    post = get_object_or_404(
        Post, pk=post_id)  
    
    # Retrieve comments that match the current post's ID
    comments = Comment.objects.filter(post=post)
    
    ctx = {"post": post, "comments": comments}
    return render(request, "blog/detail.html", ctx)


def comment(request, post_id):
    post = get_object_or_404(
        Post, pk=post_id)  
    return render(request, "blog/add-comment.html", {"post": post})


def submit_comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    author = request.user  # Use the currently logged-in user as the author
    text = request.POST.get('text')
    Comment.objects.create(author=author, text=text, post=post, pub_date = timezone.now())
    # Use reverse with the correct view name and pass post_id as a keyword argument
    url = reverse('blog:detail', kwargs={'post_id': post_id})
    return HttpResponseRedirect(url)


def add_like(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    # Check if the user already liked the post
    if request.user.liked_posts.filter(pk=post.id).exists():
        # User already liked the post, so unlike it
        post.liked_by.remove(request.user)
    else:
        # Add the like
        post.liked_by.add(request.user)

    
    url = reverse('blog:detail', kwargs={'post_id': post_id})
    return HttpResponseRedirect(url)

