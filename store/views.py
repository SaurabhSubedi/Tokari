from django.shortcuts import render,redirect
from .models import *
from django.http import JsonResponse
import json
from django.views.generic import DetailView
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Customer,Inquiry
# Create your views here.
def store(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order,created = Order.objects.get_or_create(customer=customer,complete = False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
        
        
    else:
        messages.warning(request,"You can only add to cart after you login/signup ")
        items = []
        order = {'get_cart_total':0,'get_cart_items': 0}
        cartItems = order['get_cart_items']

    products = Product.objects.all()
    clothes = Product.objects.filter(category="Clothes")
    electronics = Product.objects.filter(category= "Electronics")
    jerseys = Product.objects.filter(category= "Jerseys")
    others = Product.objects.filter(category="others")

    context = {'products':products,'cartItems':cartItems,'clothes':clothes,'electronics':electronics,'jerseys':jerseys,'others':others,}
    return render(request,'store/store.html',context)
def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order,created = Order.objects.get_or_create(customer=customer,complete = False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
        
        
    else:
        items = []
        order = {'get_cart_total':0,'get_cart_items': 0}
        cartItems = order['get_cart_items']
    context = {'items': items,'order':order,'cartItems':cartItems}
    return render(request,'store/cart.html',context)
def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order,created = Order.objects.get_or_create(customer=customer,complete = False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
        context = {'items': items, 'order': order, 'cartItems': cartItems, }
        
        
    else:
        items = []
        order = {'get_cart_total':0,'get_cart_items': 0}
        cartItems = order['get_cart_items']
        context = {'items': items,'order':order,'cartItems':cartItems,}
    return render(request,'store/checkout.html',context)

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print(f'Action:{action}')
    print(f'Product:{productId}')
    customer = request.user.customer
    product = Product.objects.get(id = productId)
    order,created = Order.objects.get_or_create(customer=customer,complete = False)
    orderItem,created = OrderItem.objects.get_or_create(order=order,product=product)
    if action == 'add':
        orderItem.quantity = (orderItem.quantity)+1
    elif action=='remove':
        orderItem.quantity = (orderItem.quantity)-1
    
    orderItem.save()
    if orderItem.quantity <= 0:
        orderItem.delete()


    return JsonResponse("item was added",safe=False)

class ProductDetail(DetailView):
    model = Product
    template_name = 'store/productdetail.html'

def logout_view(request):
    logout(request)
    return redirect('store')

def login_view(request):
    if ( request.method == "POST"):
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('store')
        else:
            messages.warning(request,"Please enter valid credentials")

    return render(request,'store/login.html')

def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        first_name = request.POST.get("firstname")
        last_name = request.POST.get("lastname")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        if (User.objects.filter(username = username).exists()):
            messages.warning(request,"Username already exists")
        else:
            if(password1 == password2):
                user = User.objects.create_user(username=username,email=email)
                user.set_password(password1)
                user.first_name = first_name
                user.last_name = last_name
                user.save()
                customer = Customer(user = user, name = username,email=email)
                customer.save()
                return redirect('login')
            else:
                messages.warning(request,"The two passwords didn't match")
    return render(request,'store/signup.html')

def about_view(request):
    return render(request,'store/about.html')
def contact_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        name = request.POST.get("name")
        myuser = request.POST.get("is_user")
        if(myuser == "True"):
            is_user = True
        else:
            is_user = False
        type = request.POST.get("type")
        desc = request.POST.get("desc")
        obj = Inquiry(email=email,name=name,is_registered=is_user,issue_type=type,description=desc)
        obj.save()
        messages.success(request,"Your query has been submitted to our team. We will get back to  you soon..")

    return render(request,'store/contacts.html')