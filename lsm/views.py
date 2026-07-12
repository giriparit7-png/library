from django.shortcuts import render,get_object_or_404,redirect
from .models import Book
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User
# Create your views here.

def Home(request):
    return render(request,"home.html")

def register(request):

    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        return redirect("UserPage")

    return render(request,"register.html")


def logout_page(request):

    logout(request)

    return redirect("login")
def login_page(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect("UserPage")

        else:
            return render(request, "login.html", {
                "error":"Invalid Username or Password"
            })

    return render(request, "login.html")


@login_required
def DashBoard(request):
    book_data=Book.objects.all()
    context={"bd":book_data}
    return render(request,"dashboard.html",context)

def Borrow_page(request,B_id):
    book=get_object_or_404(Book,B_id=B_id)

    if request.method=='POST':
        book.status=False
        book.save()
        return redirect("DashBoard")
    return render(request,"borrow.html",{"book":book})

def Return_Book(request,B_id):
    book=get_object_or_404(Book,B_id=B_id)

    if request.method=="POST":
        book.status=True
        book.save()
        return redirect("DashBoard")
    return render(request,"return.html",{"book":book})

def User_profile(request):
    return render(request,"user.html")
