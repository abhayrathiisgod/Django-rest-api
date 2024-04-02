from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.ProductListCreateApiView.as_view()), # empty because the base already has trailing / so... double
    path('<int:pk>/', views.ProductDetailApiView.as_view()),
]
