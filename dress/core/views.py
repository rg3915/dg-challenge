from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy as r
from django.views.generic import CreateView, ListView, DetailView
from django.views.generic import UpdateView, DeleteView
from django.db.models import Q
from .mixins import NameSearchMixin
from .models import Customer, Dress, Order
from .forms import CustomerForm, DressForm, OrderForm


def home(request):
    return render(request, 'index.html')


class CustomerList(NameSearchMixin, ListView):
    model = Customer
    paginate_by = 5


customer_detail = DetailView.as_view(model=Customer)

customer_create = CreateView.as_view(model=Customer, form_class=CustomerForm)

customer_update = UpdateView.as_view(model=Customer, form_class=CustomerForm)

customer_delete = DeleteView.as_view(
    model=Customer, success_url=r('core:customer_list'))


class DressList(ListView):
    model = Dress
    paginate_by = 5

    def get_queryset(self):
        queryset = super(DressList, self).get_queryset()
        q = self.request.GET.get('search_box')
        if q:
            return queryset.filter(dress_model__icontains=q)
        return queryset


dress_detail = DetailView.as_view(model=Dress)

dress_create = CreateView.as_view(model=Dress, form_class=DressForm)

dress_update = UpdateView.as_view(model=Dress, form_class=DressForm)

dress_delete = DeleteView.as_view(
    model=Dress, success_url=r('core:dress_list'))


class OrderList(ListView):
    model = Order
    paginate_by = 10

    def get_queryset(self):
        queryset = super(OrderList, self).get_queryset()
        q = self.request.GET.get('search_box')
        if q:
            return queryset.filter(
                Q(customer__icontains=q) |
                Q(dress__icontains=q) |
                Q(price__icontains=q))
        return queryset


order_detail = DetailView.as_view(model=Order)

order_create = CreateView.as_view(model=Order, form_class=OrderForm)

order_update = UpdateView.as_view(model=Order, form_class=OrderForm)

order_delete = DeleteView.as_view(
    model=Order, success_url=r('core:order_list'))
