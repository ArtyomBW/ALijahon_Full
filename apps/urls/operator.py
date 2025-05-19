from django.urls import path
from apps.views import OperatorOrderListView

urlpatterns = [
    path("operator/panel", OperatorOrderListView.as_view(), name='operator'),
]