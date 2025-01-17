class MenuItem:
    def __init__(self, item_id, name, price):
        self.item_id = item_id
        self.name = name
        self.price = price
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.last = None

    def add_item(self, item_id, name, price):
        new_item = MenuItem(item_id, name, price)
        if not self.last:
            self.last = new_item
            self.last.next = self.last
        else:
            new_item.next = self.last.next
            self.last.next = new_item
            self.last = new_item

    def display_menu(self):
        if not self.last:
            print("Menu is empty.")
            return
        current = self.last.next
        while True:
            print(f"{current.item_id}: {current.name} - ${current.price}")
            current = current.next
            if current == self.last.next:
                break

class CircularQueue:
    def __init__(self, max_size):
        self.queue = [None] * max_size
        self.front = self.rear = -1
        self.max_size = max_size

    def enqueue(self, order_id, details):
        if (self.rear + 1) % self.max_size == self.front:
            print("Queue full")
            return
        if self.front == -1:
            self.front = 0
        self.rear = (self.rear + 1) % self.max_size
        self.queue[self.rear] = (order_id, details)
        print(f"Order {order_id} added")

    def dequeue(self):
        if self.front == -1:
            print("Queue empty")
            return
        order = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.max_size
        print(f"Order {order[0]} processed")

    def display_orders(self):
        if self.front == -1:
            print("No orders")
            return
        i = self.front
        while True:
            print(f"Order ID: {self.queue[i][0]}, Details: {self.queue[i][1]}")
            if i == self.rear:
                break
            i = (i + 1) % self.max_size

if __name__ == "__main__":
    menu = CircularLinkedList()
    menu.add_item(1, "Pizza", 12.99)
    menu.add_item(2, "Burger", 8.99)
    menu.display_menu()

    orders = CircularQueue(3)
    orders.enqueue(101, "Pizza")
    orders.enqueue(102, "Burger")
    orders.display_orders()
    orders.dequeue()
    orders.display_orders()
