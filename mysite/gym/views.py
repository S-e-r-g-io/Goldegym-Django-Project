from django.shortcuts import render
from django.http import HttpResponse
from .models import Cliente, Abbonamento, Sala
# Create your views here.

def sala_view(request, *args, **kwargs):
    queryset = Sala.objects.all()
    my_context = {
        "list" : queryset
    }
    return render(request,"sala.html", my_context)
