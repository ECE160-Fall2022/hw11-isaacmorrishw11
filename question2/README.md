## Question 2

From CS102 Final 2021

## Royal Flush

Write the Python program that will solve the following question. Remember, indentation is an important aspect of Python.

A popular card game that is played is called Poker. You decide to make a mobile app called “Royal Flush”. The objective of the game is to receive a Royal Flush in a hand of 5 from a standard deck of playing cards. A Royal Flush is obtained when a player has 5 cards that have the same card suite and have the following card values: 10, J, Q, K, A.

You will write the infrastructure and logic of this mobile app with a Python class.

Create a Card class with the following members:
- card value (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K)
- card suite (clubs, spades, diamonds, hearts)

The following are functions of the Card class (note, arguments are not provided below; you need to determine them on your own):
- \_\_init\_\_ – initializes the Card class

Create a Hand class with the following members:
- player name
- hand of 5 cards

The following are functions of the Hand class (note, arguments are not provided below; you need to determine them on your own):
- \_\_init\_\_ – initializes the Hand class with 5 cards
- isRoyalFlush – determines if the hand is a Royal Flush

Simulate a basic game of poker where a player receives a Royal Flush:
- Instantiate 5 Cards with the following properties:
  - 10, hearts
  - J, hearts
  - Q, hearts
  - K, hearts
  - A, hearts
- Instantiate a player’s Hand with the following properties:
  - name: Mimi
  - the above instantiated cards
- Check that the hand is a Royal Flush by calling isRoyalFlush.
- Print out “Royal Flush” if the hand is a Royal Flush.


Execution Steps: 

Output:
