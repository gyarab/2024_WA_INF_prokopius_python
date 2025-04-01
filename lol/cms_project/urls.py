from django.urls import include, path

urlpatterns = [
    path("", include("heroes.urls")),
]