#coding: utf-8 

import random
ITENSPRINCE = {1:45,2:23,3:45,4:67,5:77}
ORDERS = {}
class Order:
    def __init__(self,order_id,order_items,order_status='Preparing'):
        self.order_id = order_id
        self.order_status = order_status
        self.order_items = order_items
        self.order_Price = self._generateCost()
        self.pickUp = False
    def __str__(self):
        return f"Order: {self.order_id} \n Status: {self.order_status} \n Quant Itens: {len(self.order_items)} \n Price: $ {self.order_Price:.2f} \n"
    
    def ModifyOrderItem(self,newItens,oldItem=None):
        if not self.pickUp:
            if len(newItens) == len(self.order_items):
                new_items = {x:newItens for x in self.order_items}
                self.order_Price = self._generateCost()
            else:
                print("Itens requested doesn't fill the all order")
            if oldItem is not None:
                for item in oldItem:
                    index = self.order_items.index(item)
                    self.order_items[index] = item
                self.order_Price = self._generateCost()
            
    def UpdateStatusOrder(self,status,pickUp=False):
        if pickUp:
            self.pickUp = True
            self.order_status = status
        self.order_status = status

    def CancelOrder(self):
        if not self.pickUp:
            self.order_status = "Canceled"
        else:
            print("Order already picked up")
    
    def _generateCost(self):
        price = 0
        for item in self.order_items:
            price += ITENSPRINCE[item]
        return price

    def OrderBillGenerate(self):
        if self.order_Price > 1000 :
             total_Amount = self.order_Price * 1.1
        else:
             total_Amount = self.order_Price * 1.05
        
        print(f"Your bill amount is: $ {total_Amount:.2f}")

def generateOrder():
    id = random.randrange(10000,99999)
    itens = []
    print("Please type each Item you with or q quit")
    for key in ITENSPRINCE:
        print(f"Item: {key} : {ITENSPRINCE[key]}")
    while True:
        reply = input("Item requested: ")
        if reply.isnumeric():
            reply = int(reply)
            if reply in itens:
                print("Item has been already added")
                continue
            if reply in ITENSPRINCE.keys():
                itens.append(reply)
                continue
            else:
                print("Item doesn't exist")
                continue
        
        if reply.lower() == "q":
            break
    order = Order(id,itens)
    print(f"the order {order.order_id} has been created the satus is: {order.order_status}")
    ORDERS[id] = order

def updateStatus(order_id):
    status = input("What is the Order Status: ")
    pickUpConfirm = input(" Do you wish to confirm the pickUp: (Y - N): ")
    if pickUpConfirm.upper() == "Y":
        ORDERS[order_id].UpdateStatusOrder(status,True)
    else:
        ORDERS[order_id].UpdateStatusOrder(status)

def modifyItens(order_id):
    alterateAllItens = input("Do you wish to Change All Itens? (Y - N)")
    if alterateAllItens.upper() == "Y":
        itens = []
        while len(itens) != len(ORDERS[order_id].order_items):
            reply = input("What Item do you wish to add? (type the id:) ")
            if reply.isnumeric():
                reply = int(reply)
                itens.append(reply)
                continue
            else:
                print("Please only type numbers")
        ORDERS[order_id].ModifyOrderItem(itens)
        print("All itens updated with success")
    elif alterateAllItens.upper() == "N":
        reply = input("What item do you wish to switch?: ")
        updated = False
        while not updated:
            reply2 = input("What is the new item?: ")
            if int(reply2) in ITENSPRINCE.keys():
                if reply.isnumeric() and reply2.isnumeric():
                    reply , reply2 = int(reply), int(reply2)
                    ORDERS[order_id].ModifyOrderItem(reply2,reply)
                    print(f"the item: {reply} was switched to {reply2} with succes")
                    updated = True
            else:
                print("Please type an item in the list")
    else:
        print("Please only type Y or N")
            
def run():
    while True:
        request = input("What your wish: ")
        if request.isnumeric():
            if int(request) == 1:
                generateOrder()
            elif int(request) == 2:
                order_id = input("What Order do you Wish to update the Status? (type the id:) ")
                if order_id.isnumeric():
                    order_id = int(order_id)
                    if order_id in ORDERS.keys():
                            updateStatus(order_id)
                            continue
                    else:
                            print("Order not found")
            elif int(request) == 3:
                order_id = input("What Order do you Wish to change de item(ns)? (type the id:) ")
                if order_id.isnumeric():
                    order_id = int(order_id)
                    if order_id in ORDERS.keys():
                            modifyItens(order_id)
                            continue
                    else:
                            print("Order not found")
            elif int(request) == 4:
                order_id = input("What Order do you wish to cancel? (type the id:) ")
                if order_id.isnumeric():
                    order_id = int(order_id)
                    if order_id in ORDERS.keys():
                            ORDERS[order_id].CancelOrder()
                            continue
                    else:
                            print("Order not found")
            elif int(request) == 5:
                order_id = input("What Order do you wish to recieve the bill? (type the id:) ")
                if order_id.isnumeric():
                    order_id = int(order_id)
                    if order_id in ORDERS.keys():
                            ORDERS[order_id].OrderBillGenerate()
                            continue
                    else:
                            print("Order not found")
            elif int(request) == 6:
                order_id = input("What Order do you wish to see details? (type the id:) ")
                if order_id.isnumeric():
                    order_id = int(order_id)
                    if order_id in ORDERS.keys():
                            print(ORDERS[order_id])
                            continue
            else:
                 print("Request not found")
        elif request.lower() == 'q':
             print("Thank you, see you soon!")
             break
        else:
            print("Please type a valid number")

def main():
    welcome = "Welcome to the Order Selector"
    print("*"*len(welcome))
    print(welcome)
    print("*"*len(welcome))
    print("Type 1 to Create an Order ") #done
    print("Type 2 to Update Status of the Order ") # done
    print("Type 3 to modify an Item in the the Order ") #done
    print("Type 4 to Cancel the Order") # done
    print("Type 5 to Generate your Bill")
    print("Type 6 to see order Status")
    print("Type q to end the system!")
    run()
if __name__ == "__main__":
    main()
