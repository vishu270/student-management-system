# print("hello world from code.py")
# # variable

# x=25 
# print(x)
# y=10
# print(x+y)
# z=x-y   
# print(z)

# # opps (object oriented programing)
class  online_store:
    count = 0

    def __init__(self, name , price):
        self.name = name
        self.price = price
        online_store.count += 1

    def get_info(self):
        print(f"price of {self.name} is {self.price}")

    @classmethod    
    def get_count(cls):
        print(f"total items in store is {cls.count}")

    @staticmethod
    def discount(price, percentage):
        print(f"discounted price of {price} is {price - price * (percentage / 100)}")

store1= online_store("laptop", 1000)
store2 = online_store("phone", 500)
store3 = online_store("tablet", 300)

store1.get_info()
store2.get_info()   
store3.get_info()

store1.discount(10000, 10) 

online_store.get_count()