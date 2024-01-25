MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


class CoffeeMachine:
  def __init__(self):
    self.money = 0
    self.resources = resources

  def get_status(self):
    for ingredient in self.resources:
      print(f"{ingredient}: self.resources[ingredient]")

  def manage_money(self, cost):
    self.money += cost

  def convert_money(self, penny, dime, nickel, quarter):
    self.money += 0.01 * penny + 0.1 * dime + 0.05 * nickel + 0.25 * quarter

  def check_resoureces(self, drink):
    for ingredient in MENU[drink]:
      if MENU[drink][ingredient] > self.resources[ingredient]:
        print(f"Sorry there is not enough {ingredient}")

  def refund_amount(self, paid_amount, drink):
    to_refund =  paid_amount - MENU[drink]["cost"]
    in_quaters = to_refund  % 25
    in_dime = (to_refund - 25 * in_quaters) % 10
    in_nickel = (to_refund - 25 * in_quaters - 10 * in_dime) % 5
    in_pennies = (to_refund - 25 * in_quaters - 10 * in_dime - 5 * in_nickel)
    
    print(f"Here is your Change : {in_quaters}quater, {in_dime}dime, {in_nickel}nickel, {in_pennies}penny")
      

print("Welcome to the coffee machine!")
user = input("What would you like? (espresso/latte/cappuccino/):")


