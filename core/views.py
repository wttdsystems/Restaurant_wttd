from collections import defaultdict

from django.shortcuts import render

tabs_values = defaultdict(int)
def index(request):
    return render(request, 'index.html')
