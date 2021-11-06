from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse

def post_list(request):
    return render(request, 'blog/post_list.html', {})