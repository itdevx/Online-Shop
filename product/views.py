from django.shortcuts import render
from django.views.generic import View


class IndexView(View):
    template_name = 'index.html'

    def get(self, request):
        return render(request ,self.template_name)


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