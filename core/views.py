from django.shortcuts import render
from collections import defaultdict

tabs_values = defaultdict(int)
def index(request):
    if request.method == 'POST':
        tab = request.POST.get('tab')
        value = request.POST.get('value')
        
        tabs_values[tab] += int(value)
        print(tabs_values)

    return render(request, 'pedidos_form.html',{'total': tabs_values})
