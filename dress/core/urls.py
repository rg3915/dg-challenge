from django.conf.urls import include, url
from dress.core import views as c
from dress.core import graphics as g

customer_patterns = [
    url(r'^$', c.CustomerList.as_view(), name='customer_list'),
    url(r'^add/$', c.customer_create, name='customer_add'),
    url(r'^(?P<pk>\d+)/$', c.customer_detail, name='customer_detail'),
    url(r'^(?P<pk>\d+)/edit/$', c.customer_update, name='customer_edit'),
    url(r'^(?P<pk>\d+)/delete/$', c.customer_delete, name='customer_delete'),
    url(r'^customer_per_size_json/$', g.customer_per_size_json),
]

dress_patterns = [
    url(r'^$', c.DressList.as_view(), name='dress_list'),
    url(r'^add/$', c.dress_create, name='dress_add'),
    url(r'^(?P<pk>\d+)/$', c.dress_detail, name='dress_detail'),
    url(r'^(?P<pk>\d+)/edit/$', c.dress_update, name='dress_edit'),
    url(r'^(?P<pk>\d+)/delete/$', c.dress_delete, name='dress_delete'),
]

order_patterns = [
    url(r'^$', c.OrderList.as_view(), name='order_list'),
    url(r'^add/$', c.order_create, name='order_add'),
    url(r'^(?P<pk>\d+)/$', c.order_detail, name='order_detail'),
    url(r'^(?P<pk>\d+)/edit/$', c.order_update, name='order_edit'),
    url(r'^(?P<pk>\d+)/delete/$', c.order_delete, name='order_delete'),
]

urlpatterns = [
    url(r'^$', c.home, name='home'),
    url(r'^customer/', include(customer_patterns)),
    url(r'^dress/', include(dress_patterns)),
    url(r'^order/', include(order_patterns)),
]
