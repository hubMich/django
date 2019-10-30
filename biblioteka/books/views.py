from django.contrib import messages
from django.core import serializers
import json
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.urls import reverse
from django.http import JsonResponse
from books.forms import AuthorForm
from .models import Author,Book
from django.db.models import Q
from django.views import generic
# Create your views here.
def index(request):
    template = loader.get_template("books/index.html")
    
def books_list(request):

    books = Book.objects.all()
    if 'q' in request.GET:
        query = request.GET.get('q')
        books = books.filter(Q(title__icontains=query) | Q(author__firstname__icontains=query))

    if 'format' in request.GET:
        format = request.GET.get('format')
        if format == 'json':
           data = serializers.serialize('json', books)
           return JsonResponse(json.loads(data), safe=False)

    context = {'books': books}
    return render(
        request,
        "books/books_list.html",
        context,
    )

def book_details(request, book_id):
    book = get_object_or_404(Book, pk=book_id)

    if request.method == "POST":
        if 'loan' in request.POST:
            messages.add_message(request, messages.SUCCESS, "Wypożyczyłeś książkę!")
            book.is_avaiable = False
        elif 'loan_back' in request.POST:
            messages.add_message(request, messages.WARNING, "Zwróciłeś książkę!")
            book.is_avaiable = True

            
    context = {'book': book}
    return render(
        request,
        "books/books_details.html",
        context,
    )

def loan(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if book.is_avaiable:
        book.is_avaiable = False
        book.save()
    else:
        pass
    return HttpResponseRedirect(reverse("books:details", args= (book_id,)))

def loan_back(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if not book.is_avaiable:
        book.is_avaiable = True
        book.save()
    else:
        pass
    return HttpResponseRedirect(reverse("books:details", args=(book_id,)))

def author_form_test(request):
    form = AuthorForm()
    return render(
        request,
        'accounts/login.html',
        context = {'form': form}
    )