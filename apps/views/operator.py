from django.views.generic import TemplateView, ListView

from apps.models import Order


class OperatorOrderListView(ListView):
    queryset = Order.objects.filter(status=Order.StatusType.NEW)
    template_name = 'apps/operator/operator-page.html'
    context_object_name = 'orders'

    def get_context_data(self, **kwargs):
        data = super().get_context_data()
        data['status'] = Order.StatusType.values
        return data