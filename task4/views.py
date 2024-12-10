from django.shortcuts import render

def index_view(request):
    return render(request, 'fourth_task/game.html')

def shop_view(request):
    games = ["Atomic Heart", "Cyberpunk 2077"]
    return render(request, 'fourth_task/shop.html', {'games': games})

def cart_view(request):
    return render(request, 'fourth_task/cart.html')
