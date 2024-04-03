from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.product_alt_view), # empty because the base already has trailing / so... double 
    path('<int:pk>/', views.product_alt_view),
]
 