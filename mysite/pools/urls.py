from django.urls import path
from . import views
app_name = "pools"
urlpatterns = [
        # pools
        path("", views.index, name="index"),
        #path("", views.IndexView.as_view(), name="index"),
        # pools/5
        path("<int:question_id>/", views.detail, name="detail"),
        # pools/5/results
        path("<int:question_id>/results/" , views.results, name="results"),
        # pools/5/vote
        path("<int:question_id>/vote/" , views.vote, name="vote"),
]

