from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
def view_bag(request):
    """A view that renders the users shopping cart"""
    return render(request, 'shopping_bag/bag.html')