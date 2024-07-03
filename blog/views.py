from django.shortcuts import render

from .models import Post


def index(request):
    posts = Post.objects.all().order_by('-pk')
    return render(
        request=request,
        template_name='blog/index.html',
        context={
            'posts': posts
        }
    )


def single_post_page(request):
    return None