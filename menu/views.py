__author__ = 'marc'
from django.views.generic import ListView
from django.shortcuts import render
from django.template import RequestContext
from cart import Cart
from menu.models import Menu
from orders.models import Otable
class MenuListView(ListView):
    model = Menu

    def get_queryset(self):
        return Menu.objects.all()

class TableListView(ListView):
    model = Otable
    template_name = 'menu/table_list.html'
    def get_queryset(self):
        return Otable.objects.all()

    def get(self, request, **kwargs):
        return render(request, self.template_name,
            {
                'objects': self.get_queryset(),
                'menu_name': kwargs['menu_name'],
            },
            context_instance=RequestContext(request))


def select_table(request, menu_name, table_name):
    menu = Menu.objects.filter(name=menu_name)
    return render(request, 'orders/menu_cart.html',
        {
            'menu': menu[0],
            'entrees': menu[0].entrees.all(),
            'menu_name': menu_name,
            'table_name': table_name,
            'cart': Cart(request),
        },
        context_instance=RequestContext(request))