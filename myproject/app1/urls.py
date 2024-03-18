from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.user_login),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('home/',views.home,name='home'),
    path('addcategory/',views.category_form,name='addcategory'),
    path('category_list/', views.category_list, name='category_list'),
    path('add_regular_product/', views.product_regularform, name='add_regular_product'),
    path('add_model_product/', views.product_modelForm, name='add_model_product'),
    path('product_list/', views.product_list, name='product_list'),
    path('file_list/', views.file_list, name='file_list'),
]