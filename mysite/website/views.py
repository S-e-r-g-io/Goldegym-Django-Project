from django.shortcuts import render
from .models import Cliente
from .forms import ClienteModelForm
# Create your views here.
def cliente_create_view(request):
    form = ClienteModelForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        'form' : form
    }
    return render(request, "cliente/create.html", context)


def cliente_detail_view(request):
    obj = Cliente.objects.get(id=1)
#    context = {
#       'title' : obj.nome,
#      'description' : obj.cf,
# }
    context = {
        'object' : obj,
    }
    return render(request, "cliente/details.html", context)