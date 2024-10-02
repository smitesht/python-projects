# Online Shopping Cart Project

## Introduction
The Online Shopping Cart project is a software implementation of a typical e-commerce system, where customers can add products to their cart and apply additional services such as gift wrapping and express delivery. 

## Problem Statement
The objective of the project is to build a flexible shopping cart system where different kinds of products (e.g., books, electronics) can be purchased and additional features like Gift Wrapping and Express Delivery can be applied.

## Solution Design
The project is designed around the Decorator Pattern to add features like gift wrapping and express delivery in a clean and modular way. The core objects, such as Books and Electronics, implement common interfaces but can be extended using decorators that add features like GiftWrapperDecorator and ExpressDeliveryDecorator.

## UML Design

![Screenshot 2024-10-02 151248](https://github.com/user-attachments/assets/659591dd-bc0c-4ad1-9b92-344a8195b6f1)

## Code

```python
from abc import ABC, abstractmethod

# interfaces
class IItem(ABC):
    @abstractmethod
    def getId(self):
      pass
    
    @abstractmethod
    def getTitle(self):
      pass

    @abstractmethod
    def getPrice(self):
      pass

    @abstractmethod
    def getDescription(self):
      pass

class IBook(ABC):
  @abstractmethod
  def getAuthor(self):
    pass

  @abstractmethod
  def getISBN(self):
    pass


class IElectronics(ABC): 
  @abstractmethod
  def getManufacturer(self):
        pass

```
```python
class Book(IItem, IBook):

  def __init__(self, id, title, price, author, isbn):
     self.bookId = id
     self.bookTitle = title
     self.bookPrice = price
     self.bookAuthor = author
     self.bookISBN = isbn

  def getId(self):
    return self.bookId

  def getTitle(self):
    return self.bookTitle

  def getPrice(self):
    return self.bookPrice

  def getDescription(self):
    return f"{self.bookTitle} by {self.bookAuthor}, Price: ${self.bookPrice}"

  def getAuthor(self):
    return self.bookAuthor

  def getISBN(self):
    return self.bookISBN
```

```python
class Electronics(IItem, IElectronics):
  def __init__(self, id, title, price, manufacturer):
    self.itemId = id
    self.itemTitle = title
    self.itemPrice = price
    self.itemManufacturer = manufacturer

  def getId(self):
    return self.itemId
  
  def getTitle(self):
    return self.itemTitle
  
  def getPrice(self):
    return self.itemPrice
  
  def getDescription(self):
    return f"{self.itemTitle} by {self.itemManufacturer}, Price: ${self.itemPrice}"
 
  def getManufacturer(self):
    return self.itemManufacturer
```

```python
# Decorator Base Class

class ItemDecorator(IItem):

  def __init__(self, item):
    self.item = item

  def getId(self):
    return self.item.getId()
  
  def getTitle(self):
    return self.item.getTitle()
  
  def getPrice(self):
    return self.item.getPrice()

  def getDescription(self):
    return self.item.getDescription()
```

```python
class GiftWrapperDecorator(ItemDecorator):

  def getPrice(self):
    return self.item.getPrice() + 2.0 # Add $2 for gift wrapping
    
  def getDescription(self):
    return f"{self.item.getDescription()} (Gift Wrapped Charged $2 Extra)"
```

```python
class ExpressDeliveryDecorator(ItemDecorator):

  def getPrice(self):
    return self.item.getPrice() + 5.0 # Add $5 for express delivery
    
  def getDescription(self):
    return f"{self.item.getDescription()} (Express Delivery Charged $5 Extra) Total Price:${self.getPrice()}"
```

```python

if __name__ == "__main__":

  harryPotter = Book(1,"Harry Potter and the Sorcerer's Stone",20.0,"J. K. Rowling","ABCD1110011")
  giftWrappedBook = GiftWrapperDecorator(harryPotter)
  expressDelivery = ExpressDeliveryDecorator(giftWrappedBook)
  print(expressDelivery.getDescription()) 

  iPhone16Pro = Electronics(2,"iPhone 16 Pro",300.0,"Apple")
  expressDelivery = ExpressDeliveryDecorator(iPhone16Pro)
  print(expressDelivery.getDescription())

```
OUTPUT
==========
Harry Potter and the Sorcerer's Stone by J. K. Rowling, Price: $20.0 (Gift Wrapped Charged $2 Extra) (Express Delivery Charged $5 Extra) Total Price:$27.0
iPhone 16 Pro by Apple, Price: $300.0 (Express Delivery Charged $5 Extra) Total Price:$305.0

