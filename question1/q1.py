import math

class CreditCard():
  def __init__(self, name, balance, points):
    self.owner = name.capitalize()
    self.balance = round(balance, 2)
    self.points = points
    
  def __add_points(self, spent, category):
    if category == "GROCERY" or category == "DINING":
      self.points += math.floor(spent) * 4
    else:
      self.points += math.floor(spent)
      
  def use_card(self, chargeAmt, category):
    self.balance += chargeAmt
    self.__add_points(chargeAmt, category.upper())

  def __str__(self):
    return "Cardholder: " + self.owner + "\nStatement Balance: " + str(round(self.balance, 2)) + "\nPoints Available: " + str(self.points)

YCard = CreditCard("Yuu", 50, 50)
YCard.use_card(25, "grocery")
print(YCard.points)
