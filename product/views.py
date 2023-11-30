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