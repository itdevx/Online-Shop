from django.shortcuts import render
from django.views.generic import View
from product.models import Product, Category


class IndexView(View):
    template_name = 'index.html'

    def get(self, request):
        new_product = Product.objects.filter(status=1).all()[:8]

        context = {
            'new_product': new_product
        }
        return render(request ,self.template_name, context)


class ProductDetailView(View):
    template_name = 'product-detail.html'

    def get(self, request):
        return render(request ,self.template_name)
    

class CartView(View):
    template_name = 'cart.html'

    def get(self, request):
        return render(request ,self.template_name)


class CheckOutView(View):
    template_name = 'checkout.html'

    def get(self, request):
        return render(request ,self.template_name)


class OrderView(View):
    template_name = 'order.html'

    def get(self, request):
        return render(request ,self.template_name)


class WishlistView(View):
    template_name = 'wishlist.html'

    def get(self, request):
        return render(request ,self.template_name)
    
    
class ShopListView(View):
    template_name = 'shop.html'

    def get(self, request):
        return render(request ,self.template_name)
    

class AboutUsView(View):
    template_name = 'about.html'

    def get(self, request):
        return render(request ,self.template_name)
    

class ContactUsView(View):
    template_name = 'contact.html'

    def get(self, request):
        return render(request ,self.template_name)