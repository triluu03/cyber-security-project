from django.forms import ValidationError
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from pathlib import Path
import sqlite3

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Book
from .forms import CreateBookForm

# Create your views here.
@login_required(login_url='/login/')
def home(request):
    books = Book.objects.all()
    return render(request, 'books/home.html', {'books': books})

def users_view(request):
    users = User.objects.all()
    return render(request, 'books/users.html', {'users': users})

def create_book(request):
    if request.method == 'POST':
        form = CreateBookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            # Add here the fix for flaw 4: Security Logging and Monitoring Failure
            pass
    else:
        form = CreateBookForm()
    return render(request, 'books/create_book.html', {'form': form})

def create_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        try:
            user = User.objects.get(username=username)
            raise ValidationError('Username already exists')
        except:
            user = User.objects.create_user(username, email, password)
            user.save()
            return redirect('login')
    else:
        return render(request, 'books/create_user.html')
