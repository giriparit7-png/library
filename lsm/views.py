from datetime import date

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import Book, BorrowedBook


# Home Page
def Home(request):
    return render(request, "home.html")


# Register User
def register(request):

    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        return redirect("login")

    return render(request, "register.html")


# Login User
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
                "error": "Invalid Username or Password"
            })

    return render(request, "login.html")


# Logout User
def logout_page(request):

    logout(request)

    return redirect("login")


# Dashboard
@login_required
def DashBoard(request):

    books = Book.objects.all()

    context = {
        "bd": books
    }

    return render(request, "dashboard.html", context)


# User Profile
@login_required
def User_profile(request):

    borrowed_books = BorrowedBook.objects.filter(
        user=request.user,
        returned=False
    )

    return render(request, "user.html", {
        "borrowed_books": borrowed_books
    })


# Borrow Book
@login_required
def Borrow_page(request, B_id):

    book = get_object_or_404(Book, B_id=B_id)

    if request.method == "POST":

        if book.status:

            BorrowedBook.objects.create(
                user=request.user,
                book=book,
                due_date=date.today()
            )

            book.status = False
            book.save()

            return redirect("UserPage")

        else:

            return render(request, "borrow.html", {
                "book": book,
                "error": "This book is currently unavailable."
            })


    return render(request, "borrow.html", {
        "book": book
    })


# Return Book
@login_required
def Return_Book(request, B_id):

    book = get_object_or_404(Book, B_id=B_id)

    if request.method == "POST":

        book.status = True
        book.save()

        return redirect("UserPage")


    return render(request, "return.html", {
        "book": book
    })