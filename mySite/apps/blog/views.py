from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.utils import timezone

from .models import Post

def index(request):
    posts = Post.objects.order_by('-published_date')[:10]
    return render(request, 'base.html', {'posts': posts})
