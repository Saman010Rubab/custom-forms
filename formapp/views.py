from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Product
from .forms import ProductForm

class ProductListView(ListView):
    model = Product
    template_name = 'formapp/product_list.html'
    context_object_name = 'products'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'formapp/product_detail.html'
    context_object_name = 'product'

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'formapp/product_form.html'
    success_url = reverse_lazy('formapp:product_list')

    # def form_valid(self, form):
    #     instance= form.save(commit=False)
    #     # Additional logic if needed
    #     instance.save()
    #     return super().form_valid(form)

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'formapp/product_form.html'
    success_url = reverse_lazy('formapp:product_list')

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'formapp/product_confirm_delete.html'
    success_url = reverse_lazy('formapp:product_list')










# class ProductUpdateView(generic.RetrieveUpdateDestroyView):
#     model = Product
#     form_class = ProductForm
#     template_name = 'form.html'
#     success_url = reverse_lazy('fromapp:update')  # Replace with your success URL

    # Optional: Define get_object to further customize the object retrieval
    # def get_object(self):
    #     pk = self.kwargs.get("pk")
    #     return get_object_or_404(YourModel, pk=pk)


def show(request):
    print("fromapp running")
    return HttpResponse("running")