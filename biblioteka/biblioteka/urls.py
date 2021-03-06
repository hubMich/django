"""biblioteka URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.contrib import admin
from django.urls import path
import accounts.views
from books.views import author_form_test

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name="books/index.html")),
    path('books', include("books.urls")),
    path('logout/', accounts.views.logout_user, name="logout"),
    path('login/', accounts.views.login_user, name="login"),
    path('testform/', author_form_test),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
