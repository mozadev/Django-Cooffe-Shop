from django.views.generic import DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import Order
from .forms import OrderProductForm


class MyOrderView(LoginRequiredMixin, DetailView):
    model = Order
    template_name = 'orders/my_order.html'
    context_object_name = 'order'

    def get_object(self, queryset=None):
        return Order.objects.filter(
            is_active=True,
            user=self.request.user
            ).first()


class CreateOrderProductView(CreateView):
    template_name = 'orders/create_order_product.html'
    form_class = OrderProductForm
    success_url = reverse_lazy('my_order')

    def get_object(self, queryset=None):
        return Order.objects.create(user=self.request.user)
