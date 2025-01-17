class Deque:
    def __init__(self, max_size):
        self.deque = [None] * max_size
        self.front = -1
        self.rear = -1
        self.max_size = max_size

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.max_size == self.front

    def add_front(self, order_id, details):
        if self.is_full():
            print("Deque full. Cannot add order at the front.")
            return
        if self.is_empty():
            self.front = self.rear = 0
        else:
            self.front = (self.front - 1 + self.max_size) % self.max_size
        self.deque[self.front] = (order_id, details)
        print(f"Order {order_id} added to the front.")

    def add_rear(self, order_id, details):
        if self.is_full():
            print("Deque full. Cannot add order at the rear.")
            return
        if self.is_empty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.max_size
        self.deque[self.rear] = (order_id, details)
        print(f"Order {order_id} added to the rear.")

    def remove_front(self):
        if self.is_empty():
            print("Deque empty. No order to remove from the front.")
            return
        order = self.deque[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.max_size
        print(f"Order {order[0]} removed from the front.")
        return order

    def remove_rear(self):
        if self.is_empty():
            print("Deque empty. No order to remove from the rear.")
            return
        order = self.deque[self.rear]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.rear = (self.rear - 1 + self.max_size) % self.max_size
        print(f"Order {order[0]} removed from the rear.")
        return order

    def display(self):
        if self.is_empty():
            print("No orders in the deque.")
            return
        print("Orders in Deque:")
        i = self.front
        while True:
            print(f"Order ID: {self.deque[i][0]}, Details: {self.deque[i][1]}")
            if i == self.rear:
                break
            i = (i + 1) % self.max_size
if __name__ == "__main__":
    orders = Deque(4)
    orders.add_rear(301, "2x Tacos")
    orders.add_front(302, "1x Pasta")
    orders.add_rear(303, "1x Pizza")
    orders.display()
    orders.remove_front()
    orders.add_front(304, "3x Burgers")
    orders.remove_rear()
    orders.display()
