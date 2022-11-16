## Question 1

From CS102 Final 2020

## Credit Cards

Credit card companies have lots of bonuses nowadays to get you to use their cards. Write a Python CreditCard class to simulate how credit cards work.

The following are members of your class:
- owner name
- current balance (in dollars)
- total points

The following are functions of the class (note, arguments are not provided below; you need to determine them on your own):
- ```__init__``` -- this function initializes the credit card
- ```__add_points``` -- adds bonus points based on the category and amount charged
  - If the category is “Grocery”, add 4x points per dollar to the total points
  - If the category is “Dining”, add 4x points per dollar to the total points
  - All other categories, add 1x point per dollar
- ```use_card``` -- this function adds the amount charged to the current balance and calls the __add_points function to add points

Simulate a use of this credit card with the following:
- Instantiate a CreditCard with the following properties:
  - owner name: Yuu
  - current balance: 50
  - total points: 50
- Use the card for a “Grocery” purchase of $25.
- Print out the total number of points after this purchase.


Execution Steps: 

Output:
