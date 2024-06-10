from store import models    

class Cart():
    def __init__(self, request):
        self.session = request.session
        self.request = request
        cart = self.session.get('session_key')
        if 'session_key' not in request.session:
            cart = self.session['session_key'] ={}
        self.cart = cart
    
    def db_add(self, product, quantity):
        product_id = str(product)
        product_qty = str(quantity)
        if product_id in self.cart:
            pass
        else:
            # self.cart[product_id] = {'price':str(product.ProdPrice)}
            self.cart[product_id] = int(product_qty)
        self.session.modified = True
        if self.request.user.is_authenticated:
            currentUser = models.Profile.objects.filter(user__id=self.request.user.id)
            carty = str(self.cart)
            carty = carty.replace("\'", "\"")
            currentUser.update(old_cart=str(carty))

    def add(self, product, quantity):
        product_id = str(product.id)
        product_qty = str(quantity)
        if product_id in self.cart:
            pass
        else:
            # self.cart[product_id] = {'price':str(product.ProdPrice)}
            self.cart[product_id] = int(product_qty)
        self.session.modified = True
        if self.request.user.is_authenticated:
            currentUser = models.Profile.objects.filter(user__id=self.request.user.id)
            carty = str(self.cart)
            carty = carty.replace("\'", "\"")
            currentUser.update(old_cart=str(carty))

    def __len__(self):
        return len(self.cart)
    
    def getProd(self):
        product_id = self.cart.keys()
        products = models.Product.objects.filter(id__in=product_id)
        return products
    
    def getQuants(self):
        quantities = self.cart
        return quantities
    
    def update(self, product, quantity):
        product_id = str(product)
        product_qty = int(quantity)
        updcart = self.cart
        updcart[product_id] = product_qty
        self.session.modified = True
        thing = self.cart
        
        return thing
    
    def delete(self, product):
        product_id = str(product)
        if product_id in self.cart:
            del self.cart[product_id]
        
        self.session.modified = True
        if self.request.user.is_authenticated:
            currentUser = models.Profile.objects.filter(user__id=self.request.user.id)
            carty = str(self.cart)
            carty = carty.replace("\'", "\"")
            currentUser.update(old_cart=str(carty))
    
    def cartTotal(self):
        product_ids = self.cart.keys()
        products = models.Product.objects.filter(id__in=product_ids)
        quantities = self.cart
        total = 0
        
        for key, value in quantities.items():
            key = int(key)
            for product in products:
                if product.id == key:
                    if product.ProdOnSale == True:
                        total += (product.ProdSalePrice * value)
                    else:    
                        total += (product.ProdPrice * value)  
        return total