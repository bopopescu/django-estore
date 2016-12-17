from django.db.models import Q
from django.http import Http404
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

# Create your views here.

from .models import Product

class ProductListView(ListView):
    model = Product

    def get_context_data(self, *args, **kwargs):
        context = super(ProductListView, self).get_context_data(*args, **kwargs)
        context["now"] = timezone.now()
        context["query"] = self.request.GET.get("q")
        return context

    def get_queryset(self, *args, **kwargs):
        query_set = super(ProductListView, self).get_queryset(*args, **kwargs)
        query = self.request.GET.get("q")
        if query:
            query_set = self.model.objects.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query)
            )
        return query_set

class ProductDetailView(DetailView):
    model = Product


def product_detail_view_func(request, id):
    #product_instance = Product.objects.get(id=id)
    #product_instance = get_object_or_404(Product, id=id)
    try:
        product_instance = Product.objects.get(id=id)
    except Product.DoesNotExist:
        raise Http404
    except:
        raise Http404
    template = "products/product_detail.html"
    context = {
        object: product_instance
    }
    return render(request, template, context)