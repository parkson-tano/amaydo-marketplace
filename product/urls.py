from django.urls import path
from .views import *
from accounts.views import *
import random
app_name = 'amydo'

urlpatterns = [
    path('', IndexView.as_view(), name='index' ),
    path('addproduct', AddProductView.as_view(), name='add_product'),
    path('product', ProductDetailView.as_view(), name='product_detail'),
    path('order-history', OrderHistoryView.as_view(), name='order_history'),
    path('my-product', UserProductView.as_view(), name='my_product'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('profile', UserProfileView.as_view(), name='profile'),
    path('account-balance', AccountBalanceView.as_view(), name='account_balance'),
    path('my-account', MyAccountView.as_view(), name='my_account'),
    path('cart', CartView.as_view(), name='my-cart'),
    path('checkout', CheckOutView.as_view(), name='checkout'),
    path('category', CategoryView.as_view(), name='category'),
]