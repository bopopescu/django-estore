from django.contrib import messages
from django.db.models import Q
from django.http import Http404
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

# Create your views here.

from .forms import VaraitionInventoryFormSet
from .mixins import StaffRequiredMixin
from .models import Product, Variation


class VariationListView(StaffRequiredMixin, ListView):
    model = Variation
    queryset = Variation.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(VariationListView, self).get_context_data(*args, **kwargs)
        context["formset"] = VaraitionInventoryFormSet(queryset=self.get_queryset())
        return context

    def get_queryset(self, *args, **kwargs):
        query_set = super(VariationListView, self).get_queryset(*args, **kwargs)
        query = self.request.GET.get("q")
        product_pk = self.kwargs.get("pk")
        if product_pk:
            product = get_object_or_404(Product, pk=product_pk)
            query_set = Variation.objects.filter(product=product)
        return query_set

    def post(self, request, *args, **kwargs):
        formset = VaraitionInventoryFormSet(request.POST, request.FILES)
        print request.POST
        if formset.is_valid():
            formset.save(commit=False)
            for form in formset:
                new_item = form.save(commit=False)
                product_pk = self.kwargs.get("pk")
                product = get_object_or_404(Product, pk=product_pk)
                new_item.product = product
                new_item.save()

            messages.success(request, "Your inventory and pricing has been updated")
            return redirect("products")
        print request.POST
        raise Http404

class ProductListView(ListView):
    model = Product
    queryset = Product.objects.all()

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