from django.urls import path

from . import views

app_name = "my_app"  # name space
urlpatterns = [
    path("", views.home, name="home"),  # pointing to home view
    path("new_search", views.new_search, name="new_search"),
]
