from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("users/", views.users_view, name="users"),
    path("create_book/", views.create_book, name="create_book"),
    path("create_user/", views.create_user, name="create_user"),
    path("delete_book/<int:book_id>/", views.delete_book, name="delete_book"),
]