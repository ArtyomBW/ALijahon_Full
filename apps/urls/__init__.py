from apps.urls.product import urlpatterns as product_url
from apps.urls.market import urlpatterns as market_url
from apps.urls.order import urlpatterns as order_url
from apps.urls.user import urlpatterns as user_url

urlpatterns = [
    *product_url,
    *market_url,
    *order_url,
    *user_url,
]
