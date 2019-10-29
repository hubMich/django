from django.urls import path
from .views import books_list
from . import views
app_name="books"
urlpatterns = [
        path("", views.books_list, name="list"),
        path("/<int:book_id>", views.book_details, name="details"),
        path("/<int:book_id>/loan", views.loan, name="loan"),
        path("/<int:book_id>/loan_back", views.loan_back, name="loan_back"),
]

