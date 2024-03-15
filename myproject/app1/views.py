from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Category, Product
from .forms import CategoryForm, ModelProductForm, RegularProductForm


# Create your views here.
def home(request):
    return render(request, 'home.html')


def category_form(request):
    category_form = CategoryForm
    if request.method == "POST":
        category_form = CategoryForm(request.POST)
        if category_form.is_valid():
            category_form.save()
            return redirect('category_list')

    return render(request, 'add_category.html', {'category_form': category_form})

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category.html', {'categories': categories})


def product_regularform(request):
    if request.method == "POST":
        form = RegularProductForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            image = form.cleaned_data['image']
            Product.objects.create(name=name, description=description, price=price, image=image)
            return redirect('product_list')
    else:
        form = RegularProductForm()
    return render(request, 'product_regularform.html', {'form': form})

def product_modelForm(request):
    if request.method == "POST":
        form = ModelProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ModelProductForm()
    return render(request, 'product_modelform.html', {'form': form})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def file_list(request):
    products = Product.objects.all()
    return render(request, 'file_list.html', {'products': products})






