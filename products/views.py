from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category

# Create your views here.
def all_products(request):
    """A view to show all products, including sorting and search queries"""
    
    products = Product.Objects.all()
    query = None
    categories = None
    
    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)
            
        if 'q' in request.GET:
            query = request.get['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            
            queries = Q(name_icontains=query) | Q(description_icontains=query)
            products = product.filter(queries)
            
                
    context = {
        'products': products,
        'search_term': query,
    }
    
    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """A view to show specific product details"""
    
    products = get_object_or_404(Product, pk=product_id)
    
    context = {
        'products': product,
        'search_term': query,
        'current_categories': categories,
    }
    
    return render(request, 'products/product_detail.html', context)