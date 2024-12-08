from abc import ABC, abstractmethod

# Abstract Class
class MenuComponent(ABC):
    @abstractmethod
    def print(self):
        pass

# Leaf Node or Leaf Class or Individual Class
class MenuItem(MenuComponent):
    def __init__(self, name, price ):
        self.itemName = name
        self.itemPrice = price

    def print(self):
        print(f"{self.itemName}.................${self.itemPrice:.2f}")

# Composite Class
class MenuCategory(MenuComponent):
    def __init__(self, categoryName):
        self.categoryName = categoryName
        self.menuItems = []

    def addItem(self, menuItem):
        self.menuItems.append(menuItem)

    def removeItem(self, menuItem):
        self.menuItems.remove(menuItem)

    def print(self):
        print(f"\n{self.categoryName}")
        for menuItem in self.menuItems:
            menuItem.print()

# Composite Class
class ComboMenuCategory(MenuComponent):
    def __init__(self, comboName, comboPrice):
        self.comboName = comboName
        self.comboPrice = comboPrice
        self.menuItems = []

    def addItem(self, menuItem):
        self.menuItems.append(menuItem)

    def removeItem(self, menuItem):
        self.menuItems.remove(menuItem)

    def print(self):
        print(f"\n{self.comboName}............${self.comboPrice}")
        for menuItem in self.menuItems:
            print(f"{menuItem.itemName}")


# main function
if __name__ == "__main__":
    
    
    vegPizza  = MenuItem("Vegi. Pizza", 20.00)
    chickenPizza = MenuItem("Chicken Pizza", 25.50)

    garlicBread = MenuItem("Garlic Bread", 5.00)
    chickenNugget = MenuItem("Chicken Nugget",6.50)

    coke = MenuItem("Coke",1.50)
    pepsi = MenuItem('Pepsi',1.50)


    pizzaCategory = MenuCategory("Pizza")
    pizzaCategory.addItem(vegPizza)
    pizzaCategory.addItem(chickenPizza)

    sideDish = MenuCategory("Side Dishes")
    sideDish.addItem(garlicBread)
    sideDish.addItem(chickenNugget)

    beverages = MenuCategory("Beverages")
    beverages.addItem(coke)
    beverages.addItem(pepsi)

    vegMealCombo = ComboMenuCategory("Veg. Meal Combo",25.00)
    vegMealCombo.addItem(vegPizza)
    vegMealCombo.addItem(garlicBread)
    vegMealCombo.addItem(coke)

    chickenMealCombo = ComboMenuCategory("Chicken Meal Combo",31.00)
    chickenMealCombo.addItem(chickenPizza)
    chickenMealCombo.addItem(chickenNugget)
    chickenMealCombo.addItem(pepsi)

    restaurantMenu = MenuCategory("Awesome Pizza Restaurant")
    restaurantMenu.addItem(pizzaCategory)
    restaurantMenu.addItem(sideDish)
    restaurantMenu.addItem(beverages)
    restaurantMenu.addItem(vegMealCombo)
    restaurantMenu.addItem(chickenMealCombo)

    restaurantMenu.print()