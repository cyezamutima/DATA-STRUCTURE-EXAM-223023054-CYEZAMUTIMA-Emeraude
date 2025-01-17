class TreeNode:
    def __init__(self, name, level="Category"):
        self.name = name
        self.level = level 
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def display(self, depth=0):
        print("  " * depth + f"{self.level}: {self.name}")
        for child in self.children:
            child.display(depth + 1)

if __name__ == "__main__":
    
    menu = TreeNode("Restaurant Menu")
    appetizers = TreeNode("Appetizers")
    main_course = TreeNode("Main Course")
    beverages = TreeNode("Beverages")

    menu.add_child(appetizers)
    menu.add_child(main_course)
    menu.add_child(beverages)
    veg_appetizers = TreeNode("Vegetarian", "Subcategory")
    non_veg_appetizers = TreeNode("Non-Vegetarian", "Subcategory")

    veg_appetizers.add_child(TreeNode("Spring Rolls", "Item"))
    veg_appetizers.add_child(TreeNode("Garlic Bread", "Item"))
    non_veg_appetizers.add_child(TreeNode("Chicken Wings", "Item"))
    non_veg_appetizers.add_child(TreeNode("Prawn Tempura", "Item"))

    appetizers.add_child(veg_appetizers)
    appetizers.add_child(non_veg_appetizers)
    main_course.add_child(TreeNode("Margherita Pizza", "Item"))
    main_course.add_child(TreeNode("Grilled Chicken", "Item"))
    main_course.add_child(TreeNode("Pasta Carbonara", "Item"))
    beverages.add_child(TreeNode("Lemonade", "Item"))
    beverages.add_child(TreeNode("Iced Tea", "Item"))
    beverages.add_child(TreeNode("Coffee", "Item"))
    print("Restaurant Menu Hierarchy:")
    menu.display()
