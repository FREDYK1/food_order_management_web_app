from django.urls import path
from . import views


urlpatterns = [
    path('', views.MenuList.as_view(), name='home'),
    path("order/<int:pk>/", views.MenuItemDetail.as_view(), name="order_detail"),
]