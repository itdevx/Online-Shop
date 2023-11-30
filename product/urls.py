from django.urls import path
from product.views import *

app_name = 'product'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]