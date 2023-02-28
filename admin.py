class FoodItem:

    def __init__(self,name,quantity,price,discount,stock):
        self.food_ID = None
        self.name = name
        self.qunatity = quantity
        self.price = price
        self.discount = discount
        self.stock = stock

    def __str__(self):
        return f"FOOD_ID: {self.food_ID}\nFOOD NAME: {self.name}\nQUNATITY: {self.qunatity}\nPRICE: {self.price}\nDISCOUNT: {self.discount}\nSTOCK: {self.stock}"


    def get_name(self):
        return self.name
    def set_name(self,new_name):
        self.name = new_name

    def get_qunatity(self):
        return self.qunatity
    def set_qunatity(self,new_qunatity):
        self.qunatity = new_qunatity

    def get_price(self):
        return self.price
    def set_price(self,new_price):
        self.price = new_price

    def get_discount(self):
        return self.discount
    def set_discount(self,new_discount):
        self.discount = new_discount

    def get_stock(self):
        return self.stock
    def set_stock(self,new_stock):
        self.stock = new_stock

class Restaurant:
        
        def __init__(self):
            self.food_items = []
            self.food_ID_count = 1
    
        def add_food_item(self):
            name = input("Enter food item name: ")
            quantity = input("Enter food item quantity: ")
            price = float(input("Enter food item price: "))
            discount = float(input("Enter food item discount: "))
            stock = int(input("Enter food item stock: "))
            food_item = FoodItem(name=name,quantity=quantity,price=price,discount=discount,stock=stock)
            food_item.food_ID = len(self.food_items) + 1
            self.food_items.append(food_item)
            print("Food item added successfully with ID:", food_item.food_ID)

        def edit_food_item(self):
            food_ID = int(input("Enter food item ID to edit: "))
            for food_item in self.food_items:
                if food_item.food_ID == food_ID:
                    name = input("Enter food item name: ")
                    quantity = input("Enter food item quantity: ")
                    price = float(input("Enter food item price: "))
                    discount = float(input("Enter food item discount: "))
                    stock = int(input("Enter food item stock: "))
                    food_item.name = name
                    food_item.quantity = quantity
                    food_item.price = price
                    food_item.discount = discount
                    food_item.stock = stock
                    print("Food item updated successfully.")
                    return
                print("Food item not found.")

        def view_food_item(self):
            for food_item in self.food_items:
                print("Food ID:",food_item.food_ID)
                print("Name:",food_item.name)
                print("Quantity:",food_item.quantity)
                print("Price INR",food_item.price)
                print("Discount:",food_item.discount)
                print("Stock:",food_item.stock)

        def remove_food_item(self):
            for food_item in self.food_items:
                food_ID = int(input("Enter food item ID to remove: "))
                if food_item.food_ID == food_ID:
                    self.food_items.remove(food_item)






    



