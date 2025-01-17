class CircularQueue:
    def __init__(self, max_size):
        self.queue = [None] * max_size
        self.front = -1
        self.rear = -1
        self.max_size = max_size

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.max_size == self.front

    def enqueue(self, order_id, details):
        if self.is_full():
            print("Queue is full. Cannot add more orders.")
            return
        if self.is_empty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.max_size
        self.queue[self.rear] = (order_id, details)
        print(f"Order {order_id} added to the queue.")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. No orders to process.")
            return
        order = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.max_size
        print(f"Order {order[0]} processed and removed from the queue.")
        return order

    def display(self):
        if self.is_empty():
            print("No orders in the queue.")
            return
        print("Current Orders in Queue:")
        i = self.front
        while True:
            print(f"Order ID: {self.queue[i][0]}, Details: {self.queue[i][1]}")
            if i == self.rear:
                break
            i = (i + 1) % self.max_size
if __name__ == "__main__":
    orders = CircularQueue(5)  
    orders.enqueue(401, "1x Cheeseburger")
    orders.enqueue(402, "2x Tacos")
    orders.enqueue(403, "1x Pasta")
    orders.display()
    orders.dequeue()
    orders.enqueue(404, "3x Pizza")
    orders.enqueue(405, "1x Salad")
    orders.enqueue(406, "1x Sandwich")  
    orders.display()
    orders.dequeue()
    orders.display()
