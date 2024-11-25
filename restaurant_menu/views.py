from django.shortcuts import render
from django.views import generic
from  .models import Order

class MenuList(generic.ListView):
    queryset = Order.objects.order_by("date_created")
    template_name = "home.html"

class MenuItemDetail(generic.DetailView):
    model = Order
    template_name = "detail.html"
