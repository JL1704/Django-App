from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),

    path("question_form/", views.question_view, name="question_form"),
    path("success/", views.success_view, name="success"),

    path("create_choice/", views.create_choice_view, name="create_choice"),
    path("success_choice/", views.success_choice_view, name="success_choice"),
]