from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.


def logout_user(request):
    logout(request)
    messages.add_message(request, messages.INFO, "Zostałeś wylogowany")
    return redirect(reverse("books:list"))


def login_user(request):
    error = None
    if request.method == "POST":
        # username = request.POST.get("username")
        # password = request.POST.get("password")

        # user = authenticate(username=username, password=password)

        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user:
                login(request, user)
                messages.add_message(request, messages.SUCCESS, "Poprawnie zalogowano")
                return redirect(reverse("books:list"))
            else:
                error = "Błędne dane"
                messages.add_message(request, messages.ERROR, "Niepoprawne dane użytkownika")
    form = AuthenticationForm()
    return render(
        request=request,
        template_name="accounts/login.html",
        context={
            'form': form,
            'error': error,
        },
    )
