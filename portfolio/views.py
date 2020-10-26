from django.shortcuts import render
from .models import Portfolio


def homepage(request):
    portfolio = Portfolio.objects.all()
    return render(request, 'index.html', {'portfolio': portfolio})
