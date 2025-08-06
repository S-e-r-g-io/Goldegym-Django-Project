from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    my_context = {
        "my_text":"this is about us",
        "my_number":123,
        "my_list":[12,24,36]
    }
    return render(request, "home.html", my_context)

def contact_view(*args, **kwargs):
    return HttpResponse("<h1>Contact Page</h1>")