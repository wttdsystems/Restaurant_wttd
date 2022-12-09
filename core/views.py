from collections import defaultdict

from django.shortcuts import render

items = {
    'coca': 10,
    'pizza': 5,
    "hamburguer": 15,
}


tabs_count = defaultdict(dict)
tabs_values = {}


def index(request):

    if request.method == 'POST':
        tab = request.POST.get('tab')
        item = request.POST.get('item')

        try:
            tabs_count[tab][item] += 1
        except KeyError:
            tabs_count[tab][item] = 1

        try:
            tabs_values[tab] += items[item]
        except KeyError:
            tabs_values[tab] = items[item]

        print(tabs_count, tabs_values)

    return render(
        request, 
        'pedidos_form.html', 
        {
            'total': dict(tabs_values), 
            'items': items
        }
    )
