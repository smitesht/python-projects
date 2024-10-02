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

# Books Class

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

class GiftWrapperDecorator(ItemDecorator):

  def getPrice(self):
    return self.item.getPrice() + 2.0 # Add $2 for gift wrapping

  def getDescription(self):
    return f"{self.item.getDescription()} (Gift Wrapped Charged $2 Extra)"

class ExpressDeliveryDecorator(ItemDecorator):

  def getPrice(self):
    return self.item.getPrice() + 5.0 # Add $5 for express delivery

  def getDescription(self):
    return f"{self.item.getDescription()} (Express Delivery Charged $5 Extra) Total Price:${self.getPrice()}"

if __name__ == "__main__":

  harryPotter = Book(1,"Harry Potter and the Sorcerer's Stone",20.0,"J. K. Rowling","ABCD1110011")
  giftWrappedBook = GiftWrapperDecorator(harryPotter)
  expressDelivery = ExpressDeliveryDecorator(giftWrappedBook)
  print(expressDelivery.getDescription())

  iPhone16Pro = Electronics(2,"iPhone 16 Pro",300.0,"Apple")
  expressDelivery = ExpressDeliveryDecorator(iPhone16Pro)
  print(expressDelivery.getDescription())