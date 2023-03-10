from django.urls import path
from . import views
urlpatterns =[
    path('', views.index, name="Home"),
    path('index/',views.index1, name="Home render")
]