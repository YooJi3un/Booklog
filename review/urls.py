from django.urls import path
from . import views

urlpatterns = [
    path("", views.review_list, name="review_list"),
    path("<int:pk>/", views.review_detail, name="review_detail"),
    path("create/", views.review_create, name="review_create"),
    path("<int:pk>/update/", views.review_update, name="review_update"),
    path("<int:pk>/delete/", views.review_delete, name="review_delete"),
    path("tag/<str:tag>/", views.review_tag, name="review_tag"),
    # comment 삭제 url 추가
    path("<int:pk>/comment_delete/", views.review_comment_delete, name="review_comment_delete"),
]