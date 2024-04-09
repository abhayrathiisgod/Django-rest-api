from django.urls import path
from . import views

urlpatterns = [
    path('', views.SearchListview.as_view(), name='search'),

]
