from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.product_List_create_view), # empty because the base already has trailing / so... double 
    path('<int:pk>/update/', views.product_update_view),
    path('<int:pk>/delete/', views.product_destroy_view),
    path('<int:pk>/', views.product_detail_view),
]
 