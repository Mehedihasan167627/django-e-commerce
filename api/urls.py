
from django.urls import path
from .views import*

app_name="api"
urlpatterns = [
       path("products/",ProductListView.as_view(),name='product-list'),
       path("product/<int:pk>/",ProductDetailView.as_view(),name='product-detail'),
       path("category-list/<int:pk>/",SubCategoryListView.as_view(),name='sub-list'),
       path("login/",LoginView.as_view(),name="login"),
       path("order/",OrderView.as_view(),name="order"),
       
      

]

