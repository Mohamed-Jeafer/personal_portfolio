from django.shortcuts import render, get_list_or_404
from .models import Blog


def all_blogs(request):
    blog = Blog.objects.all()
    return render(request, 'all_blogs.html', {'blog': blog})


def details(request, blog_id):
    blog = get_list_or_404(Blog, pk=blog_id)
    return render(request, 'details.html', {'blog': blog})
