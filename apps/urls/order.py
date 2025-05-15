from django.urls import path

from apps.views import HomeListView, ProductListView, AuthFormView, ProfileUpdateView, LogoutView, \
    district_list, ChangePasswordFormView, wishlist, WishlistView, ProductDetailView, OrderCreateView, OrderListView, \
    MarketListView, ThreadCreateView, ThreadListView , ThreadProductDetail , SearchListView , StatisticListView , CompetitionListView

urlpatterns = [
    path("order/form", OrderCreateView.as_view(), name='order'),
    path("order/list", OrderListView.as_view(), name='order-list'),
]