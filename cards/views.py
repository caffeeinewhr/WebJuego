from django.shortcuts import render
from .models import Card  # Asegúrate de que el modelo Card esté importado

# Función para inicializar datos de cartas si no existen
def initialize_cards():
    card_data = [
        {'name': 'Card 1', 'rarity': 'common', 'cost': 1, 'image_url': 'img/card1.png'},
        {'name': 'Card 2', 'rarity': 'uncommon', 'cost': 1, 'image_url': 'img/card2.png'},
        {'name': 'Card 3', 'rarity': 'uncommon', 'cost': 2, 'image_url': 'img/card3.png'},
        {'name': 'Card 4', 'rarity': 'rare', 'cost': 3, 'image_url': 'img/card4.png'},
        {'name': 'Card 5', 'rarity': 'common', 'cost': 2, 'image_url': 'img/card5.png'},
        {'name': 'Card 6', 'rarity': 'rare', 'cost': 3, 'image_url': 'img/card6.png'},
        {'name': 'Card 7', 'rarity': 'common', 'cost': 1, 'image_url': 'img/card7.png'},
        {'name': 'Card 8', 'rarity': 'rare', 'cost': 2, 'image_url': 'img/card8.png'}
    ]
    
    if not Card.objects.exists():  # Inicializar solo si no hay cartas en la base de datos
        for card in card_data:
            Card.objects.create(**card)

def cards(request):
    initialize_cards()  # Inicializar cartas si es necesario
    
    username = request.session.get('username')
    authenticated = False
    
    if username:
        authenticated = True
    
    rarity = request.GET.get('rarity')
    cost = request.GET.get('cost')
    sort = request.GET.get('sort', 'name')  # Valor predeterminado 'name'
    
    cards = Card.objects.all()
    
    if rarity:
        cards = cards.filter(rarity=rarity)
    
    if cost:
        if cost == '4+':
            cards = cards.filter(cost__gte=4)
        else:
            cards = cards.filter(cost=cost)
    
    cards = cards.order_by(sort)
    
    context = {
        'authenticated': authenticated,
        'cards': cards
    }
    
    return render(request, 'cards.html', context)
