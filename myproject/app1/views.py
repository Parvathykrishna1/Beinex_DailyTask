from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Category, Product
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CategoryForm, ModelProductForm, RegularProductForm


# Create your views here.
def home(request):
    return render(request, 'home.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('cart')
        else:
            return render(request, 'login.html', {'error_message':'Invalid login credentials'})
    return render(request, 'login.html')

@login_required
def view_cart(request):
    print("request.session", request.session)
    request.session = {
        "id" : "101",
        "value" : "dfsagb",
        "cart" : ["dress", "phone", "book"]
    }



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






