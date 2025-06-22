from abc import ABC

class User(ABC):
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class Admin(User):
    def __init__(self,name,phone,email,address):
        super().__init__(name,phone,email,address)

    def add_employee(self,system,employee):
        system.add_employee(employee)

    def view_employee(self,system):
        system.view_employee()

    def add_new_item(self,menu,item):
        menu.add_menu_item(item)

    def view_menu(self,menu):
        menu.view_menu_item()

    def delete_item(self,menu,item):
        menu.delete_item(item)

class Employee(User):
    def __init__(self,name,phone,email,address,age,designation,salary):
        super().__init__(name,phone,email,address)
        self.age=age
        self.designation=designation
        self.salary=salary
        
class Customer(User):
    def __init__(self,name,email,phone,address):
        super().__init__(name,email,phone,address)
        self.cart=Order()

    def view_menu(self,menu):
        menu.view_menu_item()

    def add_to_cart(self,menu,item_name,quantity):
        item=menu.search_item(item_name)
        if item:
            if quantity > item.quantity:
                print(f"-- Oops!!Sorry!!Item Quantity Exceeded!! We have available {item.quantity} {item.name} --\n")
            else:
                item.quantity-=quantity
                item_copy = FoodItem(item.name, item.price, quantity)
                self.cart.add_item_to_cart(item_copy)
        else:
            print(f'-- Sorry!!Item Not Found.Please View The Menu! --\n')

    def view_cart(self):
        print(f'*** {self.name} Cart ***\n')
        print('Name\tPrice\tQuantity\n')
        for item,quantity in self.cart.orders.items():
            print(f'{item.name}\t{item.price}\t{quantity}\n')
        print(f'-- Total Price: {self.cart.total_cost} --\n')

    def pay_bill(self, amount):
        if amount < self.cart.total_cost:
            shortage = self.cart.total_cost - amount
            print(f'{shortage} tk has shortage!!\n')
        else:
            change = amount - self.cart.total_cost
            print(f'-- Bill paid!! {change} tk is returned. Thanks for coming! --\n')
            self.cart.clear()  

    def remove_from_cart(self,menu,item_name):
        found = False
        for item in list(self.cart.orders.keys()):
            if item.name.upper() == item_name.upper():
                quantity_in_cart = self.cart.orders[item]
                menu_item=menu.search_item(item.name)
                if menu_item:
                    menu_item.quantity+=quantity_in_cart
                self.cart.remove_item(item)
                print(f'-- {item.name} removed from cart and restocked in menu --\n')
                found = True
                break
        if not found:
            print(f'-- {item_name} not found in cart --\n')

class System:
    def __init__(self,tmp):
        self.tmp=tmp
        self.employees=[]
    
    def add_employee(self,employee):
        self.employees.append(employee)
        print(f'-- {employee.name} is added !! --\n')

    def view_employee(self):
        print(f'\n*** {self.tmp} Employee List ***\n')
        print('Name\tEmail\tPhone\tAddress\tAge\tDesignation\tSalary')
        for emp in self.employees:
            print(f'{emp.name}\t{emp.email}\t{emp.phone}\t{emp.address}\t{emp.age}\t{emp.designation}\t{emp.salary}')

class FoodMenu:
    def __init__(self,tmp):
        self.tmp=tmp
        self.items=[]

    def add_menu_item(self,item):
        self.items.append(item)
        print(f'-- {item.name} is added!! --\n')

    def view_menu_item(self):
        print('*** Food Menu ***\n')
        print('Name\tPrice\tQuantity\n')
        for item in self.items:
            print(f'{item.name}\t{item.price}\t{item.quantity}\n')
    
    def search_item(self,item):
        for it in self.items:
            if it.name.upper() == item.upper():
                return it
        return None
    
    def delete_item(self,item_name):
        item=self.search_item(item_name)
        if item:
            self.items.remove(item)
            print(f'-- {item_name} is removed!! --\n')
        else:
            print('-- Sorry! Item Not Found. --\n')

class FoodItem:
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity

class Order:
    def __init__(self):
        self.orders={}

    # def add_item_to_cart(self,item_name):
    #     if item_name in self.orders:
    #         self.orders[item_name]+=item_name.quantity
    #     else:
    #         self.orders[item_name]=item_name.quantity
    #     print(f'-- {item_name.name} added to cart!! --\n')
    def add_item_to_cart(self, item):
        found = False
        for existing_item in self.orders:
            if existing_item.name.lower() == item.name.lower():
                self.orders[existing_item] += item.quantity
                found = True
                break

        if not found:
            self.orders[item] = item.quantity

        print(f'-- {item.name} added to cart!! --\n')

    def remove_item(self,item_name):
        if item_name in self.orders:
            del self.orders[item_name]

    @property
    def total_cost(self):
        return sum(item.price*quantity for item,quantity in self.orders.items())

    def clear(self):
        self.orders={}


restaurant_name=input('Restaurant Name: ')
sys=System(restaurant_name)
mn=FoodMenu("chili")

def Admin_Site():
    name=input('Enter Your Name: ')
    phone=input('Enter Your Phone Number: ')
    email=input('Enter You E-mail: ')
    address=input('Enter Your Address: ')
    
    ad=Admin(name,phone,email,address)
    print(f'***** Welcome {ad.name}!! *****\n')

    while True:
        print('1) View Items')
        print('2) Add New Item')
        print('3) Delete Item')
        print('4) Add New Employee')
        print('5) View Employee')
        print('6) Exit')

        choice=int(input('Enter Your Choice: '))

        if choice == 1:
            ad.view_menu(mn)

        elif choice == 2:
            item_name=input('Enter Item Name: ')
            item_price=int(input('Enter Item Price: '))
            item_quantity=int(input('Enter Item Quantity: '))
            item=FoodItem(item_name,item_price,item_quantity)
            ad.add_new_item(mn,item)

        elif choice == 3:
            item_name=input('Enter Item Name You Want to Delete: ')
            ad.delete_item(mn,item_name)

        elif choice == 4:
            name=input("Enter Employee Name: ")
            phone=input("Enter Phone Number: ")
            email=input("Enter E-mail: ")
            address=input("Enter Address: ")
            age=input("Enter Age: ")
            designation=input("Enter Designation: ")
            salary=input("Enter Salary: ")
            emp=Employee(name,phone,email,address,age,designation,salary)
            ad.add_employee(sys,emp)

        elif choice == 5:
            ad.view_employee(sys)
        
        elif choice == 6:
            print("** Thanks For Visiting!! **\n")
            break

        else:
            print("Invalid Choice!Please Choose From 1-6.\n")

def Customer_site():
    name=input('Enter Your Name: ')
    phone=input('Enter Your Phone Number: ')
    email=input('Enter You E-mail: ')
    address=input('Enter Your Address: ')
    
    cust=Customer(name,phone,email,address)
    print(f'***** Welcome {cust.name}!! *****\n')

    while True:
        print('1) View Menu')
        print('2) Add Item To Cart')
        print('3) View Cart')
        print('4) Delete Item From Cart')
        print('5) Pay Bill')
        print('6) Exit')

        choice=int(input('Enter Your Choice: '))

        if choice == 1:
            cust.view_menu(mn)

        elif choice == 2:
            item_name=input('Enter Item Name: ')
            item_quantity=int(input('Enter Item Quantity: '))
            cust.add_to_cart(mn,item_name,item_quantity)

        elif choice == 3:
            cust.view_cart()

        elif choice == 4:
            item_name=input('Which Item Do you Want To Remove From Cart: ')
            cust.remove_from_cart(mn,item_name)

        elif choice == 5:
            amount=int(input('Enter The Amount: '))
            cust.pay_bill(amount)
        
        elif choice == 6:
            print("** Thanks For Visiting!! **\n")
            break

        else:
            print("Invalid Choice!Please Choose From 1-6.\n")

while True:
    print(f"******* Welcome To {restaurant_name}!! *******\n")
    print("1) Admin")
    print("2) Customer")
    print("3) Exit")

    choice=int(input("Enter Your Identity: "))
    
    if choice == 1:
        Admin_Site()

    elif choice == 2:
        Customer_site()

    elif choice == 3:
        print("** Thanks For Visiting!! **\n")
        break
    else:
        print("Invalid Choice!!Please Choose from 1-3\n")
