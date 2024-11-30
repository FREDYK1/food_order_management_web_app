from django.views import generic
from  .models import Order, Meal_Types

class MenuList(generic.ListView):
    queryset = Order.objects.order_by("date_created")
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["meals"] = Meal_Types
        context["Order_list"] = self.queryset
        return context

class MenuItemDetail(generic.DetailView):
    model = Order
    template_name = "detail.html"
