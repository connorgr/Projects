""" **Product Inventory Project** - Create an application which manages an
inventory of products. Create a product class which has a price, id, and
quantity on hand. Then create an *inventory* class which keeps track of various
products and can sum up the inventory value.
"""

class Product:
    def __init__(self, id, quantity, price):
        self.id = id
        self.quantity = quantity
        self.price = price
        if quantity < 0:
            raise ValueError("Product quantity must be greater than or equal to 0.")

    def __getitem__(self, name):
        if hasattr(self, name):
            if name == "id":
                return self.id
            if name == "quantity":
                return self.quantity
            if name == "price":
                return self.price
        else:
            return None

    def __repr__(self):
        return "<Product id:%s quantity:%s price:%s>" % (self.id, self.quantity, self.price)

    def __setitem__(self, name, value):
        if hasattr(self, name):
            if name == "id":
                self.id = value
            if name == "quantity":
                self.quantity = value
            if name == "price":
                self.price = value
            self[name] = value
        else:
            print "WARNING:", name, "is not a valid value."

    def __str__(self):
        return self.__repr__()

    def get(self, name):
        return self.__getitem__(name)

    def set(self, name, value):
        return self.__setitem__(name, value)

class Inventory:
    def __init__(self):
        self.__products = {}

    # Assumes that objects with the same id should update current price
    def addProduct(self, product):
        if isinstance(product, Product):
            if product["id"] not in self.__products:
                self.__products[product["id"]] = product
            else:
                inventoryObj = self.__products[product["id"]]
                inventoryObj["quantity"] = inventoryObj["quantity"] + product["quantity"]
                inventoryObj["price"] = product["price"]
        else:
            raise TypeError("addProduct requires a Product object.")

    def printInventory(self):
        print self.__products
        for k, v in self.__products.iteritems():
            print v

    def sumValue(self):
        return sum([p.price * p.quantity for k, p in self.__products.iteritems()])

if __name__ == "__main__":
    inventory = Inventory()

    inventory.addProduct(Product("Milk", 10, 2.40))
    inventory.addProduct(Product("Eggs", 20, 2.00))
    inventory.printInventory()
    print inventory.sumValue()
