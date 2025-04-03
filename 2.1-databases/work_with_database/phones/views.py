from django.shortcuts import render, redirect, get_object_or_404
from phones.models import Phone


def index(request):
    return redirect('catalog')

def show_catalog(request):
    template = 'catalog.html'
    SORTING_MAP = {
        'name': 'name',
        'min_price': 'price',
        'max_price': '-price'
    }
    sort_key = request.GET.get('sort', 'name')
    order_field = SORTING_MAP.get(sort_key, 'name')
    phones = Phone.objects.all().order_by(order_field)
    context = {'phones': phones}
    return render(request, template, context)

def show_product(request, slug):
    template = 'product.html'
    phone = get_object_or_404(Phone, slug=slug)
    return render(request, template, {'phone': phone})
