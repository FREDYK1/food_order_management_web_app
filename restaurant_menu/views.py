from django.views import generic
from  .models import Order

class MenuList(generic.ListView):
    queryset = Order.objects.order_by("date_created")
    template_name = "home.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = {"meals": "Rice"}
        return context

class MenuItemDetail(generic.DetailView):
    model = Order
    template_name = "detail.html"
