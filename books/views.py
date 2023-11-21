from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect, get_object_or_404
from pathlib import Path
import sqlite3

from django.contrib.auth.decorators import login_required
# Fix for Flaw 6: CSRF Attacks: CSRF protection
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.models import User
from .models import Book, UserInfo
from .forms import CreateBookForm

# Fix for Flaw 5: Inefficient Logging and Monitoring
"""
import logging
logger = logging.getLogger(__name__)
"""

# Fix for Flaw 6: CSRF Attacks: CSRF protection
"""
csrf_protect
"""
# Create your views here.
@login_required(login_url='/login/')
def home(request):
    books = Book.objects.all()
    return render(request, 'books/home.html', {'books': books})

# Fix for Flaw 6: CSRF Attacks: CSRF protection
"""
csrf_protect
"""
@login_required(login_url='/login/')
def users_view(request):
    users_info = UserInfo.objects.all()
    # Fix for Flaw 5: Inefficient Logging and Monitoring
    """
    logger.warning("User information is being displayed!")
    """
    return render(request, 'books/users.html', {'users': users_info})

# Fix for Flaw 3: Sensitive Data Exposure: replace the above view with the following view
"""
def users_view(request):
    users = User.objects.all().values('username', 'email')
    return render(request, 'books/users.html', {'users': users})
"""


# Fix for Flaw 6: CSRF Attacks: CSRF protection
"""
csrf_protect
"""
@login_required(login_url='/login/')
def create_book(request):
    if request.method == 'POST':
        form = CreateBookForm(request.POST)
        if form.is_valid():
            form.save()
            # Fix for Flaw 5: Inefficient Logging and Monitoring
            """
            logger.info("A new book has been created!")
            """
            return redirect('home')
        else:
            # Fix for Flaw 5: Inefficient Logging and Monitoring
            """
            logger.error("Something wrong happened! The form is not valid!")
            """
            pass
    else:
        form = CreateBookForm()
    return render(request, 'books/create_book.html', {'form': form})

# Fix for Flaw 6: CSRF Attacks: CSRF protection
"""
csrf_protect
"""
def create_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        if User.objects.filter(username=username).exists():
            raise ValidationError('Username already exists')

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
        # Fix for Flaw 5: Inefficient Logging and Monitoring
        """
        logger.info(f"A new user has been created with username: {username}")
        """

        # Fix for Flaw 3: Sensitive Data Exposure: delete two lines below
        userinfo = UserInfo(username=username, password=password, email=email)
        userinfo.save()
        return redirect('login')
    else:
        return render(request, 'books/create_user.html')

# Fix for Flaw 6: CSRF Attacks: CSRF protection
"""
csrf_protect
"""
@login_required(login_url='/login/')
def delete_book(request, book_author):
    connection = sqlite3.connect(Path(__file__).resolve().parent.parent / 'db.sqlite3')
    cursor = connection.cursor()
    query = "DELETE FROM books_book WHERE author = '%s';" % (book_author, )
    try:
        cursor.execute(query)
        connection.commit()
        connection.close()
    except:
        # Fix for Flaw 5: Inefficient Logging and Monitoring
        """
        logger.warning("Database query's failed!")
        """
        pass
    return redirect('home')

# Fix for Flaw 1: Injection
# Fix for Flaw 4: Insecure Design
# Replace the above delete_book view with the following one
"""
def delete_book(request, book_id):
    book_to_delete = get_object_or_404(Book, id=book_id)
    book_to_delete.delete()
    return redirect('home')
"""