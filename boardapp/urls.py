from django.urls import path
from . import views

urlpatterns = [
    path("", views.postList, name="postList"),
    path("create/", views.postCreate, name="postCreate"),
    path("<int:id>/", views.postView, name="postView"),
    path("update/<int:id>/", views.postUpdate, name="postUpdate"),
    path("delete/<int:id>/", views.postDelete, name="postDelete"),
    path("apiTest", views.apiTest, name="apiTest")
    # path("<int:question_id>/", views.detail, name="detail"),
    # path("<int:question_id>/results/", views.results, name="results"),
    # path("<int:question_id>/vote/", views.vote, name="vote"),
]
