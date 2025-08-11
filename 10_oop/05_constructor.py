class Chai_order:

    def __init__(self,chai_type,chai_size):
        self.chai_type = chai_type
        self.chai_size = chai_size
    def order_summary(self):
        return f"Chai Type: {self.chai_type}, Chai Size: {self.chai_size}"
    
order_1=Chai_order("Masala", "Large")
print(order_1.order_summary())

order_2=Chai_order("Ginger", "Small")
print(order_2.order_summary())        