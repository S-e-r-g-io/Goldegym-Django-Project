from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def sala_view(request, *args, **kwargs):
    my_context = {}
    return render(request,"sala.html", my_context)
