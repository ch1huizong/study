from django.urls import path

from . import views

app_name = "inventory"
urlpatterns = [
    path("", views.main, name="main"),
    path(
        "categorized/<str:category>/<int:category_id>/",
        views.categorized,
        name="categorized",
    ),
    path("server_detail/<int:server_id>/", views.server_detail, name="server_detail"),
]
