class User:

    def __init__(self,name,phone_number,email,address,password):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.password = password
        self.orders = []
        self.users = []

    def register(self):
        name = input("Enter your full name: ")
        phone_number = input("Enter your phone number: ")
        email = input("Enter your email: ")
        address = input("Enter your address: ")
        password = input("Enter your password: ")
        user = User(name = name , phone_number=phone_number,email=email,address=address,password=password)
        self.users.append(user)
        print("Registration Successful.")

    def login(self):
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        for user in self.users:
            if user.email == email and user.password == password:
                 print("Login Successful.")
            else:
                print("Invaild Users email or Users password")
        
    def place_order(self):
        order_items = input("Enter the food ID separated by commas: ")
        order_items = list(map(int,order_items.split(",")))
        order_items = [self.food_items[i-1] for i in order_items]
        print("\nSelected Items: ")
        total_price = 0
        for order_item in order_items:
            print(f"{order_item.name} ({order_item.quantity}) [INR {order_item.price}]")
            total_price += order_item.price
        confirm = input("Do you want to place the order? (Y/N): ")
        if confirm.lower() == "y":
            order = {"Items": order_items, "Total_price": total_price}
            self.orders.appened(order)
            for order_item in order_items:
                order_item.stock -= 1
            print("Order Placed Successfully!!")
        else:
            print("Order Cancelled.")

    def order_history(self):
       print("ORDER HISTORY")
       if not self.orders:
           print("You have not placed any order yet.")
       else:
           for i,order in enumerate(self.orders):
               print(f"ORDER {i+1}:{[str(item) for item in order]}") 

    def update_profile(self):
        print("Enter the details to UPDATE: ")
        self.name = input("Enter NAME:")
        self.phone_number = input("Enter Phone Number: ")
        self.email = input("Enter Email: ")
        self.address = input("Enter Address: ")
        self.password = input("Enter Password: ")


    






