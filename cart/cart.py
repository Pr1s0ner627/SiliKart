from store import models    

class Cart():
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('session_key')
        if 'session_key' not in request.session:
            cart = self.session['session_key'] ={}
        self.cart = cart
    
    def add(self, product, quantity):
        product_id = str(product.id)
        product_qty = str(quantity)
        if product_id in self.cart:
            pass
        else:
            # self.cart[product_id] = {'price':str(product.ProdPrice)}
            self.cart[product_id] = int(product_qty)
        self.session.modified = True
    
    def __len__(self):
        return len(self.cart)
    
    def getProd(self):
        product_id = self.cart.keys()
        products = models.Product.objects.filter(id__in=product_id)
        return products
    
    def getQuants(self):
        quantities = self.cart
        return quantities