from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.views.generic import View, DetailView, ListView
from product.models import Product, Category
from django.shortcuts import get_object_or_404
import sweetify
from django.contrib import messages
from django.db.models import Q


class IndexView(View):
    template_name = 'index.html'

    def get(self, request):
        new_product = Product.objects.filter(status=1).all()[:8]
        category = Category.objects.all()
        print(category)
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
        loaded_product = self.object
        product_id = self.request.session.get('product_fav')
        context['is_fav'] = product_id == str(loaded_product.id)
        return context
    

class AddToFavorite(View):
    def post(self, request):
        product_id = request.POST['slug']
        request.session['product_fav'] = product_id
        return redirect('product:product-detail', product_id)


class SearchView(ListView):
    template_name = 'shop.html'
    context_object_name = 'products'
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
    def get_queryset(self):
        request = self.request
        query = request.GET.get('q')
        if query is not None:
            product_query = Q(title__icontains=query) | Q(description__icontains=query)
            return Product.objects.filter(product_query, status=True).distinct()
        

class CategoryView(ListView):
    template_name = 'shop.html'
    context_object_name = 'products'
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
    def get_queryset(self):
        slug = self.kwargs['slug']
        category = Category.objects.filter(category_name__iexact=slug).first()
        if category is None:
            return Product.objects.get_prodcut_by_category(slug)
    

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