from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Category, Product
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CategoryForm, ModelProductForm, RegularProductForm


# Create your views here.
def user_login(request):
    if request.method == 'POST':
        user = request.POST.get('username')
        pw = request.POST.get('password')
        user = authenticate(request, username=user, password=pw)
        if user is not None:
            login(request, user)
            success_logins = request.COOKIES.get('success_logins', 0)
            success_logins = int(success_logins) + 1
            response = redirect('product_list')
            response.set_cookie('success_logins', success_logins)
            return response
        else:
            request.session.setdefault('failed_login_attempts', 0)
            request.session['failed_login_attempts'] += 1
    return render(request, 'login.html', {'failed_login_attempts': request.session.get('failed_login_attempts')})

def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

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

def file_list(request):
    products = Product.objects.all()
    return render(request, 'file_list.html', {'products': products})






