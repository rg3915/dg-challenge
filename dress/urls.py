from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from .core import views

router = routers.DefaultRouter()
router.register(r'customers', views.CustomerViewSet)
router.register(r'dresses', views.DressViewSet)
router.register(r'orders', views.OrderViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'', include('dress.core.urls', namespace='core')),
    url(r'^admin/', admin.site.urls),
]
