class Order:
    def __init__(self, order_id, details, priority):
        self.order_id = order_id
        self.details = details
        self.priority = priority

    def __repr__(self):
        return f"Order ID: {self.order_id}, Details: {self.details}, Priority: {self.priority}"


def quick_sort(orders, low, high):
    if low < high:
        
        pivot_index = partition(orders, low, high)
        quick_sort(orders, low, pivot_index - 1)
        quick_sort(orders, pivot_index + 1, high)


def partition(orders, low, high):
    pivot = orders[high].priority 
    i = low - 1  

    for j in range(low, high):
        if orders[j].priority > pivot:  
            i += 1
            orders[i], orders[j] = orders[j], orders[i]  

    orders[i + 1], orders[high] = orders[high], orders[i + 1]  
    return i + 1
if __name__ == "__main__":
    
    orders = [
        Order(101, "1x Pizza", 3),
        Order(102, "2x Burgers", 1),
        Order(103, "1x Pasta", 2),
        Order(104, "3x Tacos", 5),
        Order(105, "1x Salad", 4),
    ]

    print("Unsorted Orders:")
    for order in orders:
        print(order)
    quick_sort(orders, 0, len(orders) - 1)

    print("\nSorted Orders by Priority (High to Low):")
    for order in orders:
        print(order)
