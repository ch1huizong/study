from django.urls import path

from . import views

app_name = "inventory"
urlpatterns = [
    path("", views.main, name="main"),
    path(
        "categoried/<str:category>/<int:category_id>/",
        views.categoried,
        name="categoried",
    ),
    path("server_detail/<int:server_id>/", views.server_detail, name="server_detail"),
]
