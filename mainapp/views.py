from django.shortcuts import render

# Create your views here.

def HomeView(request, *args, **kwargs):
    context = {}
    return render(request, 'index.html', context)
