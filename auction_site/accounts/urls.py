# accounts/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),  # ✅ Add this
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
from .views import (
    ProductListView, ProductCreateView, ProductUpdateView, ProductDeleteView
)

urlpatterns += [
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/create/', ProductCreateView.as_view(), name='product-create'),
    path('products/<int:pk>/update/', ProductUpdateView.as_view(), name='product-update'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product-delete'),
]
