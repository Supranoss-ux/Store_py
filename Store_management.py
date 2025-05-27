from datetime import datetime


class Person:

    def __init__(self, fname: str, lname: str, national_id: str, birthyear: str, gender: str)-> None:
        self.fname =fname
        self.lname = lname
        self.national_id = national_id
        self.birthyear = birthyear
        self.gender = gender

    def __str__(self):
        return f"{self.fname} {self.lname}\n{self.national_id}\n{self.birthyear}\t{self.gender}"

    def show_info(self)-> None:
        print("*" * 35)
        print(f"Gender: {self.gender}\nName: {self.fname} {self.lname}\nNational ID: {self.national_id}\nBirthyear: {self.birthyear}")
        print("*" * 35)


#___________________________________________________________________________________________________________________________
class Product:
    all_product = dict()

    def __init__(self, name: str, product_id: str, price: float, brand: str, weight: float)-> None:
            try:
                self.name = name
                self.product_id = product_id
                self.price = price
                self.brand = brand
                self.weight = weight
                Product.all_product[self.product_id] = [self.name, self.brand, self.price, self.weight]
                print("******Successful******")
            except AttributeError:
                pass

    @staticmethod
    def search(pr_id):
            try:
                print("-" * 35)
                if Product.all_product[pr_id]:
                    print(f"Product with this id({pr_id}): name-> {Product.all_product[pr_id][0]}\tbrand-> {Product.all_product[pr_id][1]}\tprice-> {Product.all_product[pr_id][2]}\tweight-> {Product.all_product[pr_id][3]}")
                    print("-" * 35)
                    return True
            except KeyError:
                print("Product not found !!")
                print("-" * 35)
                return False

    def _set_name(self, name):
        self._name = name

    def _set_product_id(self, product_id)-> None:
        try:
            if Product.all_product[product_id]:
                print("\t\tProduct id is already exists !!")
        except KeyError:
                self._product_id = product_id

            
    def _set_price(self, price)-> None:
        if price > 0:
            self._price = price
        else:
            print("\t\tInvalid Price !!")

    def _set_brand(self, brand):
        self._brand = brand

    def _set_weight(self, weight)-> None:
        if weight > 0:
            self._weight = weight
        else:
            print("\t\tInvalid Wieght !!")

    def _get_name(self):
        return self._name
    
    def _get_product_id(self) :
        return self._product_id

    def _get_price(self):
         return self._price

    def _get_brand(self):
        return self._brand

    def _get_weight(self):
         return self._weight

    name = property(_get_name, _set_name)
    product_id = property(_get_product_id, _set_product_id)
    price = property(_get_price, _set_price)
    weight = property(_get_weight, _set_weight)
    brand = property(_get_brand, _set_brand)


#___________________________________________________________________________________________________________________________
class Customer(Person):
    all_customers = dict()

    def __init__(self, fname, lname, national_id, birthyear, gender, customer_id: str, province: str, city: str,)-> None:
        try:
            super().__init__(fname, lname, national_id, birthyear, gender)
            self.customer_id = customer_id
            self.province = province
            self.city = city
            Customer.all_customers[self.national_id] = [self.fname, self.lname, self.birthyear, self.gender, self.customer_id, self.province, self.city]
            print("******Successful******")
        except AttributeError:
            pass

    @staticmethod
    def search(nt_id):
        try:
            print("-" * 35)
            if Customer.all_customers[nt_id]:
                print(f"Customer with this National id({nt_id}): name-> {Customer.all_customers[nt_id][0:2]}\tBirthyear-> {Customer.all_customers[nt_id][2]}\tGender-> {Customer.all_customers[nt_id][3]}\tCustomer ID-> {Customer.all_customers[nt_id][4]}\tResidence-> {Customer.all_customers[nt_id][5]} {Customer.all_customers[nt_id][6]}")
                print("-" * 35)
                return True
        except KeyError:
            print("Customer not found !!")
            print("-" * 35)
            return False

    def _set_national_id(self, national_id):
        try:
            if Customer.all_customers[national_id]:
                print("Invalid national ID")
        except KeyError:
            if len(national_id) == 10:
                self._national_id = national_id
            else:
                print("Invalid national ID")

    def _get_national_id(self):
        return self._national_id

    def __str__(self):
        return f"{self.fname} {self.lname}\n{self.national_id}\n{self.birthyear}\t{self.gender}\t{self.customer_id}\n{self.province}\t{self.city}"

    def show_info(self):
        print("*" * 35)
        print(f"Gender: {self.gender}\nName: {self.fname} {self.lname}\nNational ID: {self.national_id}\tCustomer ID: {self.customer_id}\nBirthyear: {self.birthyear}\nResidence: {self.province} {self.city}")
        print("*" * 35)

    national_id = property(_get_national_id, _set_national_id)


#___________________________________________________________________________________________________________________________
class Dealer:
    all_dealers = dict()

    def __init__(self, dealer_id: str, name: str, es_year: int, enconomic_code: str, owner_fname: str, owner_lname: str, province: str, city: str)-> None:
        try:
            self.dealer_id = dealer_id
            self.name = name
            self.es_year= es_year
            self.enconomic_code = enconomic_code
            self.owner_fname = owner_fname
            self.owner_lname = owner_lname
            self.province = province
            self.city = city
            Dealer.all_dealers[self.dealer_id] = [self.name, self.es_year, self.enconomic_code, self.owner_fname, self.owner_lname, self.province, self.city]
            print("******Successful******")
        except AttributeError:
            pass
    
    @staticmethod
    def search(dl_id):
            try:
                print("-" * 35)
                if Dealer.all_dealers[dl_id]:
                    print(f"Dealer with this id({dl_id}): name-> {Dealer.all_dealers[dl_id][0]}\tEstablished Year-> {Dealer.all_dealers[dl_id][1]}\tEconomic Code-> {Dealer.all_dealers[dl_id][2]}\tOwner Name-> {Dealer.all_dealers[dl_id][3:5]}\tResidence: {Dealer.all_dealers[dl_id][5]} {Dealer.all_dealers[dl_id][6]}")
                    print("-" * 35)
                    return True
            except KeyError:
                print("Dealer not found !!")
                print("-" * 35)
                return False

    def _set_dealer_id(self, dealer_id):
        try:
            if Dealer.all_dealers[dealer_id]:
                print("\t\tDealer id is already exists !!")
        except KeyError:
                self._dealer_id = dealer_id
    
    def _get_dealer_id(self):
        return self._dealer_id
    
    dealer_id = property(_get_dealer_id, _set_dealer_id)


class Purchase:
    all_purchase = []

    def __init__(self, nt_id: str, pr_id: str, dl_id: str, quantity: int):
        try:
            self.quantity = quantity
            if Purchase.exist(nt_id, pr_id, dl_id):
                Purchase.all_purchase.append([nt_id, dl_id, pr_id, quantity, Product.all_product[pr_id][2], datetime.now().date()])
                print("******Successful******")
        except AttributeError:
            pass

    @staticmethod
    def exist(nt_id: str, pr_id: str, dl_id: str):
        try:
            if Dealer.all_dealers[dl_id] and Customer.all_customers[nt_id] and Product.all_product[pr_id]:
                return True
        except KeyError:
            print("Customer or Product or Dealer with this ID doesent exited !!")
            return False
    
    @staticmethod
    def nsearch(nt_id: str):
        lst = []
        q = 0
        for nt in Purchase.all_purchase:
            if nt[0] == nt_id:
                q = 1
                lst.append(nt)
        if q == 0:
            return None
        else:
            return lst

    @staticmethod
    def psearch(pr_id: str):
        lst = []
        q = 0
        for pr in Purchase.all_purchase:
            if pr[2] == pr_id:
                q = 1
                lst.append(pr)
        if q == 0:
            return None
        else:
            return lst
    
    @staticmethod
    def dsearch(dl_id: str):
        lst = []
        q = 0
        for dl in Purchase.all_purchase:
            if dl[1] == dl_id:
                q = 1
                lst.append(dl)
        if q == 0:
            return None
        else:
            return lst

    @staticmethod
    def sum_quan(pr_id: str):
        lst = Purchase.psearch(pr_id)
        q = 0
        for ls in lst:
            q += ls[3]
        return q

    def _set_quantity(self, quantity)-> None:
        if quantity > 0:
            self._quantity = quantity
        else: print("Quantity is not valid!!")
    
    def _get_quantity(self):
        return self._quantity

    quantity = property(_get_quantity, _set_quantity)


while True:

    while True:
        try:
            choose = int(input("|\t1. Add a Product\n|\t2. Remove a Product\n|\t3. Add a Customer\n|\t4. Remove a Customer\n|\t5. Add a Dealer\n|\t6. Remove a Dealer\n|\t7. Record a Purchase\n|\t8. Total Purchase of Customer\n|\t9. List of Customers of a Product\n|\t10. Products Sold by a Dealer\n|\t11. Number of Sales of a Product\n|\t12. Products Purchased by a Customer\n|\t13. Sales Report by Dealer\n|\t14. Exit the Program : "))
            if choose >= 1 and choose <= 14:
                break
            else:
                print("The Number must be between 0 and 15!!!")
        except ValueError:
            print("Enter a valid number please!!")

    print("-" * 30)
    match choose:
        case 1:
            while True:
                try:
                    pname = str(input("Enter the Name of product: "))
                    pid = str(input("Enter the id of product: "))
                    pprice = float(input("Enter the Price of product: "))
                    pbrand = str(input("Enter the Brand of product: "))
                    pweight = float(input("Enter the Weight of product (g): "))
                    yn = str(input(f"Name: {pname}, ID: {pid}, Price: {pprice}, Brand: {pbrand}, Weight: {pweight}\nAre the values correct? (Yes / No): "))
                    if "y" in yn.lower():
                        pobj = Product(pname, pid, pprice, pbrand, pweight)
                        break
                except ValueError:
                    print("Price and Weight must be a number!!")
        case 2:
            while True:
                pid = str(input("Enter the id of product(c for Cancel): "))
                if "c" in pid.lower(): break
                if Product.search(pid):
                    check = str(input("Is the information correct? (Yes / No): "))
                    if "y" in check.lower():
                        del Product.all_product[pid]
                        print("******Successful******")
                        break
                        # Inja yadet nare
        case 3:
            while True:
                gender = str(input("Your Gender? (Male or Female?): "))
                cfname = str(input("Enter your first name please: "))
                clname = str(input("And the last name: "))
                ccode = str(input("Enter your Customer code: "))
                national_id = str(input("Enter your national id: "))
                birthyear = str(input("Enter your birthyear: "))
                province = str(input("Your province: "))
                city = str(input("And the city: "))
                yn = str(input(f"Gender: {gender}, Name: {cfname} {clname}, Customer Code: {ccode}, National ID: {national_id}, Birthyear: {birthyear}, Residence: {province} {city}\nAre the values correct? (Yes / No): "))
                if "y" in yn.lower():
                    cobj = Customer(cfname, clname, national_id, birthyear, gender, ccode, province, city)
                    break
        case 4:
            while True:
                national_id = str(input("Enter the National Id of Customers (c for Cancel): "))
                if "c" in national_id.lower(): break
                if Customer.search(national_id):
                    check = str(input("Is the information correct? (Yes / No): "))
                    if "y" in check.lower():
                        del Customer.all_customers[national_id]
                        print("******Successful******")
                        break
                        # va inja
        case 5:
            while True:
                try:
                    dl_id = str(input("Dealer ID : "))
                    dname = str(input("Enter the Dealer name: "))
                    es_year = int(input("Enter the Established Year: "))
                    enc_code = str(input("Enter the Enconomic Code: "))
                    owner_fname = str(input("Enter the first name of Owner: "))
                    owner_lname = str(input("Enter the last name of Owner: "))
                    dprovince = str(input("Enter the Dealer Province: "))
                    dcity = str(input("Enter the Dealer City: "))
                    yn = str(input(f"Dealer ID: {dl_id}, Dealer Name: {dname}, Established Year: {es_year}, Enconomic Code: {enc_code}, Owner Name: {owner_fname} {owner_lname}, Residence: {dprovince} {dcity}\nAre the values correct? (Yes / No): "))
                    if "y" in yn.lower():
                        dobj = Dealer(dl_id, dname, es_year, enc_code, owner_fname, owner_lname, dprovince, dcity)
                        break
                except ValueError:
                    print("Established Year must be a number!!")
        case 6:
            while True:
                dl_id = str(input("Dealer ID (c for Cancel): "))
                if "c" in dl_id.lower(): break
                if Dealer.search(dl_id):
                    check = str(input("Is the information correct? (Yes / No): "))
                    if "y" in check.lower():
                        del Dealer.all_dealers[dl_id]
                        print("******Successful******")
                        break
                        #va injaaa
        case 7:
            while True:
                try:
                    national_id = str(input("National ID: (c for cancel)"))
                    if "c" in national_id.lower(): break
                    pid = str(input("Product ID: "))
                    dl_id = str(input("Dealer ID: "))
                    quantity = int(input("Quantity : "))
                    yn = str(input(f"National ID: {national_id}, Product ID: {pid}, Dealer ID: {dl_id}, Quantity: {quantity}\nAre the values correct? (Yes / No): "))
                    if "y" in yn.lower():
                        puobj = Purchase(national_id, pid, dl_id, quantity)
                        break
                except ValueError:
                    print("Quantity must be a number!!")
        case 8:
            national_id = str(input("National ID: (c for cancel)"))
            if "c" in national_id.lower(): break
            if Purchase.nsearch(national_id) == None:
                print("Customer with this National id dont have any purchases!!")
            else:
                q = 0
                all_price = 0
                lst = Purchase.nsearch(national_id)
                print(f"Purchase reports for this customer:\nNational ID: {national_id}")
                for ls in lst:
                    q += ls[3]
                    price = ls[4] * ls[3]
                    all_price += price
                    print(f"Dealer ID: {ls[1]}, Product ID: {ls[2]}, Quantity: {ls[3]}, Price: {ls[4]}, Date: {ls[5]}")
                print("*" * 20)
                print(f"Number of purchases: {q}\nTotal amount of all purchases: {all_price}")
        case 9:
            pid = str(input("Product ID: "))
            if Purchase.psearch(pid) == None:
                print("Product with this id dont have any Purchases!!")
            else:
                lst = Purchase.psearch(pid)
                lst.pop(-1)
                print("-" * 35)
                print("Customers who bought this product: ")
                for ls in lst:
                    nt_id = ls[0]
                    print(f"Gender: {Customer.all_customers[nt_id][3]}\nName: {Customer.all_customers[nt_id][0]} {Customer.all_customers[nt_id][1]}\nNational ID: {nt_id}\nBirth Year: {Customer.all_customers[nt_id][2]}\nCustomer ID: {Customer.all_customers[nt_id][4]}\nResidence: {Customer.all_customers[nt_id][5]} {Customer.all_customers[nt_id][6]}")
                    print("-" * 20)
        case 10:
            dl_id = str(input("Dealer ID: "))
            if Purchase.dsearch(dl_id) == None:
                print("Dealer with this ID has not sold any products!!")
            else:
                lst = Purchase.dsearch(dl_id)
                print("-" * 35)
                print("Products sold by this dealership: ")
                for dl in lst:
                    pid = dl[2]
                    print(f"Product ID: {pid}\nName: {Product.all_product[pid][0]}\nBrand: {Product.all_product[pid][1]}\nPrice: {Product.all_product[pid][2]}\nWeight: {Product.all_product[pid][3]}")
                    print("-" * 20)
        case 11:
            pid = str(input("Product ID: "))
            if Purchase.psearch(pid) == None:
                print("Product with this id dont have any Purchases!!")
            else:
                lst = Purchase.psearch(pid)
                lst.pop(-1)
                print("-" * 35)
                print(f"Result for this Product id({pid}): ")
                for ls in lst:
                    print(f"Buyer: {ls[0]}\nSeller: {ls[1]}\nQuantity: {ls[3]}\nDate: {ls[5]}")
                    print("-" * 20)
            print(f"Sum of Quantity: {Purchase.sum_quan(pid)}")
        case 12: 
            national_id = str(input("National ID: "))
            if Purchase.nsearch(national_id) == None:
                print("Customer with this National id dont have any purchases!!")
            else:lst = Purchase.nsearch(national_id)
            print(f"Purchase reports for this customer:\nNational ID: {national_id}")
            for ls in lst:
                pid = ls[2]
                print(f"Product ID: {pid}\tName: {Product.all_product[pid][0]}\tBrand: {Product.all_product[pid][1]}\tPrice: {Product.all_product[pid][2]}\tWeight: {Product.all_product[pid][3]}")
                print("-" * 20)
        case 13:
            dl_id = str(input("Dealer ID: "))
            if Purchase.dsearch(dl_id) == None:
                print("Dealer with this ID has not sold any products!!")
            else:
                lst = Purchase.dsearch(dl_id)
                print("-" * 35)
                q = 0
                all_price = 0
                for ls in lst:
                    q += ls[3]
                    price = ls[3] * ls[4]
                    all_price += price
            print(f"Dealer Name: {Dealer.all_dealers[dl_id][0]}\t Dealer ID: {dl_id}\nTotal Dealer sales: {all_price}")
        case 14: break
    print("-" * 35)

print("Ended!")