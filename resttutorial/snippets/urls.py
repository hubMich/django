from django.urls import path
import snippets.views as views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.SnippetList.as_view()),
    path('<int:pk>', views.SnippetDetail.as_view()),

]


urlpatterns = format_suffix_patterns(urlpatterns)