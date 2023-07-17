from django.conf import settings

from stations.models import Station

class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)

        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        
        self.cart = cart
        
    def __iter__(self):
        for s in self.cart.keys():
            self.cart[str(s)]['station'] = Station.objects.get(pk=s)
        
        for item in self.cart.values():
            item['total_price'] = int(item['station'].price * item['quantity']) / 100

            yield item
            
    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())
    
    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True
        
    def add(self, station_id, quantity=1, update_quantity=False):
        station_id = str(station_id)
        
        if station_id not in self.cart:
            self.cart[station_id] = {'quantity': 1, 'id': station_id}
        
        if update_quantity:
            self.cart[station_id]['quantity'] += int(quantity)

            if self.cart[station_id]['quantity'] == 0:
                self.remove(station_id)
            
        self.save()
    
    def remove(self, station_id):
        if station_id in self.cart:
            del self.cart[station_id]
            self.save()
    
    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
    
    def get_total_cost(self):
        for p in self.cart.keys():
            self.cart[str(p)]['product'] = Station.objects.get(pk=p)

        return int(sum(item['product'].price * item['quantity'] for item in self.cart.values())) / 100
    
    def get_item(self, station_id):
        if str(station_id) in self.cart:
            return self.cart[str(station_id)]
        else:
            return None