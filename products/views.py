from django.shortcuts import render, get_list_or_404, redirect
from .forms import ProductForm, RawProductForm
from .models import Product, Producttype
from django.http import HttpResponse
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView,
)


# Create your views here.

def product_list_view(request):
    # objects = Product.objects.filter(summary__contains='the').values('title', 'price')
    objects = Product.objects.all().values('title', 'description', 'price', 'summary', 'featured')
    # return HttpResponse(objects)
    context = {
        'objects': objects
    }
    return render(request, "products/product_list.html", context)


# def product_create_view(request):
#     my_form = RawProductForm()
#     if request.method == "POST":
#         my_form = RawProductForm(request.POST)
#         if my_form.is_valid():
#             Product.objects.create(**my_form.cleaned_data)
#             my_form = RawProductForm()
#         else:
#             print(my_form.errors)
#     context = {
#         'form': my_form
#     }
#     return render(request, "products/product_create.html", context)

# directly from model
def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()
    context = {
        'form': form
    }
    return render(request, "products/product_create.html", context)


# def product_list_view(request):
#     objects = Product.objects.all()
#     context = {
#         'objects': objects
#     }
#     return render(request, "products/product_list.html", context)


def product_detail_view(request):
    obj = Product.objects.get(id=1)
    context = {
        'obj': obj
    }
    return render(request, "products/product_detail.html", context)


def dynamic_lookup_view(request, id):
    obj = Product.objects.get(id=id)
    # obj = get_list_or_404(Product, id=id)
    context = {
        'obj': obj
    }
    return render(request, "products/product_detail.html", context)


def product_delete_view(request, id):
    # obj = Product.objects.get(id=id)
    obj = get_list_or_404(Product, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('../')
    context = {
        'obj': obj
    }
    return render(request, "products/product_delete.html", context)
