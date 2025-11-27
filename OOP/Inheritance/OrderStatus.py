from enum import Enum
class Status(Enum):
    PENDING = 1
    PROCESSING  = 2
    SHIPPED = 3
    DELIVERED = 4
    CANCELLED = 5

class Order:
    def __init__(self,order_id,customer_name):
        self.order_id = order_id
        self.customer_name = customer_name
        self.status = Status.PENDING

    def update_status(self,new_status:Status):
        if isinstance(new_status,Status):
            self.status = new_status
        else:
            print("Wrong status")
    @property 
    def display(self):
        print("order id: ",self.order_id,"\ncustomer name: " ,self.customer_name,"\nstatus: ",self.status )

order1  = Order(1,"asliddin")
order1.update_status(Status.DELIVERED)
order1.display