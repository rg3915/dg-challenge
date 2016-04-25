from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy as r
from django.views.generic import CreateView, ListView, DetailView
from django.views.generic import UpdateView, DeleteView
from rest_framework import viewsets
from .mixins import NameSearchMixin, DressSearchMixin, OrderSearchMixin
from .models import Customer, Dress, Order
from .forms import CustomerForm, DressForm, OrderForm
from .serializers import CustomerSerializer, DressSerializer, OrderSerializer


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


class DressList(DressSearchMixin, ListView):
    model = Dress
    paginate_by = 5


dress_detail = DetailView.as_view(model=Dress)

dress_create = CreateView.as_view(model=Dress, form_class=DressForm)

dress_update = UpdateView.as_view(model=Dress, form_class=DressForm)

dress_delete = DeleteView.as_view(
    model=Dress, success_url=r('core:dress_list'))


class OrderList(OrderSearchMixin, ListView):
    model = Order
    paginate_by = 10


order_detail = DetailView.as_view(model=Order)

order_create = CreateView.as_view(model=Order, form_class=OrderForm)

order_update = UpdateView.as_view(model=Order, form_class=OrderForm)

order_delete = DeleteView.as_view(
    model=Order, success_url=r('core:order_list'))


class CustomerViewSet(viewsets.ModelViewSet):
    ''' API endpoint that allows customers to be viewed or edited. '''
    queryset = Customer.objects.all().order_by('first_name')
    serializer_class = CustomerSerializer
    authentication_classes = []
    permission_classes = []


class DressViewSet(viewsets.ModelViewSet):
    ''' API endpoint that allows dress to be viewed or edited. '''
    queryset = Dress.objects.all().order_by('dress_model')
    serializer_class = DressSerializer
    authentication_classes = []
    permission_classes = []


class OrderViewSet(viewsets.ModelViewSet):
    ''' API endpoint that allows orders to be viewed or edited. '''
    queryset = Order.objects.all().order_by('-created')
    serializer_class = OrderSerializer
    authentication_classes = []
    permission_classes = []
