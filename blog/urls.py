from django.urls import path
from .views import BlogListView
from .views import BlogPrueba

app_name="blog"

urlpatterns = [
    path('',BlogListView.as_view(), name="home"),
    path('prueba/',BlogPrueba.as_view(), name="prueba")
]
