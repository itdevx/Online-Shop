from django.urls import path
from product.views import *

app_name = 'product'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('product-detail/<slug>/', ProductDetailView.as_view(), name='product-detail'),
    path('add-to-fav/', AddToFavorite.as_view(), name='add-to-fav'),
    path('about-us/', AboutUsView.as_view(), name='about-us'),
    path('contact-us/', ContactUsView.as_view(), name='contact-us'),
    path('cart/', CartView.as_view(), name='cart'),
    path('checkout/', CheckOutView.as_view(), name='checkout'),
    path('order/', OrderView.as_view(), name='order'),
    path('wishlist/', WishlistView.as_view(), name='wishlist'),
    path('shop/', ShopListView.as_view(), name='shop'),
    path('search/', SearchView.as_view(), name='search'),
    path('category-product/<slug>/', CategoryView.as_view(), name='category'),
]