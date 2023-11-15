from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect, get_object_or_404
from pathlib import Path
import sqlite3

from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.models import User
from .models import Book
from .forms import CreateBookForm

"""
import logging
logger = logging.getLogger(__name__)
"""

# Fix for Flaw 4: Cross Site Scripting: CSRF protection
"""
csrf_protect
"""
# Create your views here.
@login_required(login_url='/login/')
def home(request):
    books = Book.objects.all()
    return render(request, 'books/home.html', {'books': books})

# Fix for Flaw 4: Cross Site Scripting: CSRF protection
"""
csrf_protect
"""
@login_required(login_url='/login/')
def users_view(request):
    users = User.objects.all()
    # Fix for Flaw 3: Sensitive Data Exposure: displaying passwords
    """
    users = User.objects.all().values("username", "email")
    """
    return render(request, 'books/users.html', {'users': users})

# Fix for Flaw 4: Cross Site Scripting: CSRF protection
"""
csrf_protect
"""
@login_required(login_url='/login/')
def create_book(request):
    if request.method == 'POST':
        form = CreateBookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            # Fix for Flaw 5: Inefficient Logging and Monitoring: logging information about errors
            """
            logger.error("Something wrong happened! The form is not valid!")
            """
            pass
    else:
        form = CreateBookForm()
    return render(request, 'books/create_book.html', {'form': form})

# Fix for Flaw 4: Cross Site Scripting: CSRF protection
"""
csrf_protect
"""
def create_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        try:
            user = User.objects.get(username=username)
            raise ValidationError('Username already exists')
        except:
            # Fix for Flaw 2: Broken Authentication: weak password
            """
            if len(password) < 8:
                raise ValidationError('Password must be at least 8 characters long')
            if not any(c.isupper() for c in password):
                raise ValidationError('Password must contain at least one uppercase character')
            if not any(c.islower() for c in password):
                raise ValidationError('Password must contain at least one lowercase character')
            if not any(c.isdigit() for c in password):
                raise ValidationError('Password must contain at least one number')
            """
            user = User.objects.create_user(username, email, password)
            user.save()
            return redirect('login')
    else:
        return render(request, 'books/create_user.html')

# Fix for Flaw 4: Cross Site Scripting: CSRF protection
"""
csrf_protect
"""
@login_required(login_url='/login/')
def delete_book(request, book_id):
    connection = sqlite3.connect(Path(__file__).resolve().parent.parent / 'db.sqlite3')
    cursor = connection.cursor()
    query = "DELETE FROM books_book WHERE id = %s;" % (book_id, )
    cursor.execute(query)
    connection.commit()
    connection.close()
    return redirect('home')

# Fix for Flaw 1: Injection: replace the above delete_book view with the following one
"""
def delete_book(request, book_id):
    book_to_delete = get_object_or_404(Book, id=book_id)
    book_to_delete.delete()
    return redirect('home')
"""