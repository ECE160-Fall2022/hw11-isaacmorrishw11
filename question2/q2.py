class Card():
  def __init__(self, value, suite):
    self.value = str(value) 
    # ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    self.suite = suite.upper()
    # ["clubs", "spades", "diamonds", "hearts"]
    

class Hand():
  def __init__(self, name, card1, card2, card3, card4, card5):
    self.name = name.capitalize()
    self.hand = [card1, card2, card3, card4, card5]
    self.RoyalFlush = ["10", "J", "Q", "K", "A"]
    
  def isRoyalFlush(self):
    suite = self.hand[1].suite
    count = 0
    
    for card in self.hand:
      if card.suite != suite or card.value not in self.RoyalFlush:
        break
      else:
        count += 1
    if count == 5:
      print("Royal Flush")

card1 = Card(10, "hearts")
card2 = Card("J", "hearts")
card3 = Card("Q", "hearts")
card4 = Card("K", "hearts")
card5 = Card("A", "hearts")

myHand = Hand("mimi", card1, card2, card3, card4, card5)
myHand.isRoyalFlush()
