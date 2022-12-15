from django.shortcuts import render
from .models import Post


def post_list(request):
    posts = Post.objects.all()
    # this goes to the db and retrieves the requested objects
    # pass these objects as context to the template
    return render(request, 'blog/post_list.html', {'posts': posts})
