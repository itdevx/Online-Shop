from typing import Any
from django.shortcuts import render
from django.views.generic import View, DetailView
from product.models import Product, Category
from django.shortcuts import get_object_or_404


class IndexView(View):
    template_name = 'index.html'

    def get(self, request):
        new_product = Product.objects.filter(status=1).all()[:8]
        category = Category.objects.all()

        context = {
            'new_product': new_product,
            'category': category
        }
        return render(request ,self.template_name, context)


class ProductDetailView(DetailView):
    template_name = 'product-detail.html'
    model = Product
    slug_url_kwarg = 'slug'
    query_pk_and_slug = True
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = get_object_or_404(Product, status=True, slug=self.kwargs['slug'])
        context['related_product'] = Product.objects.filter(category__product=product, status=True).exclude(slug=self.kwargs['slug'])[:4]
        return context


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