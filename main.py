from users import User
from admin import Restaurant
from admin import FoodItem

class Main:

    def execute(self,choice,user,restaurant):
        if choice == 1 :
            print("*"*20,"REGISTER","*"*20)
            user.register()

        elif choice == 2 :
            print("*"*20,"LOGIN","*"*20)
            user.login()

        elif choice == 3:
            print("*"*20,"PLACE NEW ORDER","*"*20)
            user.place_order()

        elif choice == 4:
            print("*"*20,"ORDER HISTORY","*"*20)
            user.order_history()

        elif choice == 5:
            print("*"*20,"UPDATE PROFILE","*"*20)
            user.update_profile()
        elif choice == 6:
            print("*"*20,"ADD FOOD ITEM","*"*20)
            restaurant.add_food_item()
        elif choice == 7:
            print("*"*20,"EDIT FOOD ITEM","*"*20)
            restaurant.edit_food_item()
        elif choice == 8:
            print("*"*20,"REMOVE FOOD ITEM","*"*20)
            restaurant.remove_food_item()
        elif choice == 9:
            print("*"*20,"VIEW FOOD ITEM","*"*20)
            restaurant.view_food_item()

        else:
            print("Invaild choice")

if __name__ == "__main__":

    main = Main()
    restaurant = Restaurant()
    fooditem = FoodItem('name','quantity','price','discount','stock')
    user = User('name','phone_number','email','address','password') 
    
    while True:
        choice = int(input("Enter \n1. TO REGISTER: \n2. LOGIN: \n3. PLACE ORDER \n4. ORDER HISTORY \n5. UPADATE PROFILE \n6. ADD_FOOD ITEM \n7. EDIT_FOOD ITEM \n8. REMOVE FOOD ITEM \n9. VIEW FOOD ITEM \n"))
        main.execute(choice=choice,user=user,restaurant=restaurant)

        