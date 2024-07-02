from django.urls import path
from .views import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView

app_name= "formapp"

urlpatterns = [
    # path("", show, name="show"),
    path('products/', ProductListView.as_view(), name='product_list'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('new/', ProductCreateView.as_view(), name='product_create'),
    path('<int:pk>/edit/', ProductUpdateView.as_view(), name='product_update'),
    path('<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    # path("update/<int:pk>", ProductUpdateView.as_view(), name="update")

]
