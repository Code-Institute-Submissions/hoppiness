from django.shortcuts import render, redirect

# Create your views here.
def view_bag(request):
    """A view that renders the users shopping cart"""
    return render(request, 'shopping_bag/bag.html')

def add_to_bag(request, item_id):
        """A view that adds an item(s) the users shopping cart"""
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST>get('redirect_url')
    bag = request.session.get('back' {})
    
    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity
        
    request.session['bag'] = bag
    return redirect(redirect_url)