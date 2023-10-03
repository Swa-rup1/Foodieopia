



from django.shortcuts import get_object_or_404, render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.http import JsonResponse
from django.contrib import messages
from django.views import View
from .forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.files.base import ContentFile
from .models import  Cart, Item, Person, Collection
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from .models import Cart, Order, OrderItem



# Create your views here.




def search_food_categories(request):
    search_query = request.GET.get("q")
    # Implement your search logic here.
    # For simplicity, we'll return a predefined list of categories that contain the search query.
    all_categories = ["MoMo", "Dessert", "Pizza", "Burger", "Pasta"]
    matching_categories = [category for category in all_categories if search_query.lower() in category.lower()]

    # Return search results as JSON
    return JsonResponse({"results": matching_categories})



# HomePage, SignUp, SignIn Views
@login_required(login_url='login')
def HomePage(request):
    return render (request,'home.html')


def fastvariety(request):
    return render (request,'fastvariety.html')

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
        



    return render (request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            request.session['person-id'] = user.id 
            login(request,user)
            messages.success(request, "Logged in successfully")
            return redirect('home')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')

def user_logout(request):
    auth_logout(request)
    return redirect('login')


def about(request):
    return render(request, "about.html")

def restaurant(request):
    return render(request, "restaurant.html")

# Shop View
def shop(request):
    collections = Collection.objects.all()
    context = {
        "details": request.session.get('person'),
        "collections": collections
    }
    print(context)
    return render(request, "shop.html", context)



#  Cart Views 



def shop(request):
    collections = Collection.objects.all()
    context = {
        "details": request.session.get('person'),
        "collections": collections
    }
    print(context)
    return render(request, "shop.html", context)


def product_details(request, id):
    collection_response = Collection.objects.get(id=id)
    item_response = Item.objects.filter(category_id=id)
    context = {
        "collection_detail": collection_response,
        "items": item_response,
        "details": request.session.get('person-id'),
    }

    return render(request, "product_details.html", context)


def view_cart(request):
    matchedCart = Cart.objects.filter(
        person_id=request.session.get('person-id'))
    # print(matchedCart)
    item_list = []
    for item in matchedCart:
      
        matched_item = Item.objects.filter(item_name=item.item_id).get()
        item_list.append(matched_item)
    # try
    # print(item_list)


    context = {
        "cartdetails": matchedCart,
        "itemdetails": item_list
    }
    return render(request, 'cart.html', context)




# Adding Functionality like add, remove, view the cart


def add_to_cart(request, product_id, item_id, item_quantity, price):
    print(item_id)
    print(product_id)
    print(item_quantity)
    print(price)
    try:
        item = Item.objects.get(pk=item_id)
        
        Cart.objects.create(
            item_id=item,
            quantity=item_quantity,
            price=price,
            person_id=request.session['person-id']  # You can adjust this as needed
        )
        messages.success(request, "Added to cart")
    except Exception as e:
        print(e)
        messages.error(request, "Couldnot add to cart")
        print("Adding failed")

    return redirect('../../../../../product_details/'+str(product_id))


def delete_cart(request, cart_id):
    try:
        Cart.objects.filter(id=cart_id).delete()
        messages.success(request, "Cart item removed successfully")
    except:
        print("cart-delete-failed")

    return redirect("cart")

def cart_view(request):
    cart_item = get_object_or_404(CartItem, user=request.user, item_id=item_id)


# def logout(request):
#     try:
#         del request.session['person']
#         del request.session['person-id']
#         messages.success(request,"logout success")
#         return redirect('login')
        
#     except:
#        messages.error(request,"logout failed")
       
#     return redirect('login')



# views.py


