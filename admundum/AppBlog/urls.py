from django.urls import path
from .views import (
    inicio,
    post_create,
    about,
    post_update,
    PosteoListView,
    PosteoDetailView,
    PosteoDeleteView
)
urlpatterns = [
    path("", inicio, name="inicio"),
    path("inicio/", inicio, name="inicio"),
    path("about/", about, name="about"),
    path("create-page/", post_create, name="post_create"),
    path("update-page/<int:id>/", post_update, name="post_update"),
    path("update-page/", post_update, name="post_update"),
    path('pages/', PosteoListView.as_view(), name='posts'),
    path("page_detail/<int:pk>/", PosteoDetailView.as_view(), name="post_detail"),
    path("delete_page/<int:pk>/", PosteoDeleteView.as_view(), name="post_delete"),

]
