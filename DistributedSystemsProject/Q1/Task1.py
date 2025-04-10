from abc import ABC, abstractmethod
import copy
import threading
#abstract class with the clone method which is defined in later functions
class ItemPrototype(ABC):
    @abstractmethod
    def clone(self):
        pass

#my item class using the absstract class and has my 3 values name amount and price of the item
class Item(ItemPrototype):
    def __init__(self, name, amount, price):
        self.name = name
        self.amount = amount
        self.price = price
      #clone function to create additional copies of itemclass to customize  
    def clone(self):
        return copy.deepcopy(self)
    #string that gets returned by calling updateitem containing the 3 class values
    def __str__(self):
        return f"Item: {self.name}, Qty: {self.amount} Price: {self.price}"
   #updateitem function which creates a clone of the protype class and then appends to newcly cloned class changing the values 
def updateItem(itemprototype: ItemPrototype):
    itemclone = itemprototype.clone() 
    itemclone.price += 10
    print("Updated Item: ", itemclone)
    #same as above just changing different object
def updateItem2(itemprototype: ItemPrototype):
    itemclone = itemprototype.clone()
    itemclone.name = "Coke"
    print("Updated Item: ", itemclone)
    #main where a item class is created and the result is then printed
    #I make 2 threads targeting both the updateitem functions and then run them
if __name__ == '__main__':
    itemproto = Item("Drink",2,5)
    print(itemproto)
    t1 = threading.Thread(target=updateItem(itemproto))
    t2 = threading.Thread(target=updateItem2(itemproto))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
        
