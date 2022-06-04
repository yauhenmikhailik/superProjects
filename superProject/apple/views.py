from django.shortcuts import render, redirect
from apple.models import Category, Product, Shop
from .forms import CategoryForm,ProductForm

def apple_page (request):
    categories = Category.objects.all()
    products = Product.objects.all()
    context = {
        'categories' : categories,
        'products': products
    }

    return render(request, 'apple.html', context)

def category_sort(request,id):
    categories = Category.objects.all()
    products = Product.objects.filter(categories=id)
    context = {"products":products,
               'categories' : categories,}

    return render(request, "categories.html",context)

def product_detail(request, id):
    product = Product.objects.get(id =id)
    shop =  product.shop_set.all

    context = {'product':product,
               'shops': shop
               }

    return render(request, 'product_detail.html', context)


def less_forms(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    shop = Shop.objects.all()
    form = CategoryForm()
    context = {
        'categories': categories,
        'products': products,
        'shop': shop,
        'form': form,
    }

    if request.method =='POST':

        title = request.POST.get('Title')
        discription = request.POST.get('discription')
        price = request.POST.get('price')
        created = request.POST.get('created')
        categories = request.POST.get('categories')
        img = request.POST.get('img')
        kind = request.POST.get('kind')
        add_forms(title,discription,price,created,categories,img,kind)

    else:
        pass

    return render(request, 'less_forms.html', context)



def less_shops(request):
    products = Product.objects.all()
    shop = Shop.objects.all()
    form = CategoryForm()
    context = {
        'products': products,
        'shop': shop,
        'form': form,
        }


    return render(request, 'less_shops.html', context)



def category_form(request):

    return redirect('apple:less_forms')

def product_form(request):

    return redirect('apple:less_forms')

def shop_form(request):

    return redirect('apple:less_forms')


def form_category(request):
    form = CategoryForm()
    context ={
        'form':form,
    }
    if request.method =='POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
        else:
            print(form.error)

    # return redirect('apple:less_forms')
    return render(request,'form_error.html', context)

def form_model(request):
    form = ProductForm()
    context ={
        'form':form,
    }
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    return render(request, 'model_form.html',context)


