from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Article
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def search(request):
    query = request.GET.get('query', '')
    posts  = Article.objects.filter(Q(title__icontains=query) | Q(text__icontains=query))
    page = request.GET.get('page', 3)
    paginator = Paginator(posts, 1)

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
        'query': query,
        'posts': posts,
    }

    return render(request, 'search.html', context)

def home(request):

    posts = Article.objects.all()
    page = request.GET.get('page', 3)
    paginator = Paginator(posts, 1)


    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
        'posts': posts,
    }

    return render(request, 'home.html', context)


def fast(request, slug):
    post = get_object_or_404(Article, slug=slug)

    context = {
        'post': post,
    }

    return render(request, 'post_detail.html', context)