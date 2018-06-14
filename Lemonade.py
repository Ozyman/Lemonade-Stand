import random
import math

class LemonadeStand:
    '''  Hold the state of the lemonade stand game '''
    def __init__(self, name):
        self.name=name
        self.money=25
        self.lemons=0
        self.temperature=90
    
    def display_state(self):
        print(" ###################################")
        print(" ## {:^12} Lemonade Stand   ##".format(self.name + "'s"))
        print(" ###################################")
        print(" ##   MONEY: ${:<5}               ##".format(str(self.money)))
        print(" ##   LEMONS: {:<5}               ##  ".format(str(self.lemons)))
        print("\n\n")
        
    def purchase(self):
        lemon_cost = round(0.2 + random.random() * 0.6,2)
        print("Lemons cost ${}".format(lemon_cost))
        number_to_purchase = input("How many would you like to purchase? ")
        total_cost = number_to_purchase * lemon_cost 
        while  total_cost > self.money:
            print("{} Lemons @ {} each is {}".format(number_to_purchase, lemon_cost, total_cost))
            print("You don't have enough money!\n")
            number_to_purchase = input("How many would you like to purchase? ")
            total_cost = number_to_purchase * lemon_cost 
        self.lemons += number_to_purchase
        self.money -= total_cost
        
    def setTemperature(self):
        min_temp = 60
        max_temp = 105
        self.temperature = random.randint(min_temp, max_temp)

    def printForecast(self):
        forecast = self.temperature + random.randint(-15,15)
        print("The temperature forecast for tomorrow is {} degrees Farenheit\n".format(forecast)) 
        
    def sell(self):
        lemonade_price = input("How much would you like to sell the Lemonade for? ")
        
        # factors range from -4 to +4
        
        price_factor = -1 * (lemonade_price - 1) / .2
        temperature_factor = (self.temperature - 80) / 7
        
        cups_demand = round(random.randint(25,50) * (1.8 ** price_factor) * (1.8 ** temperature_factor))
        
        if cups_demand < self.lemons * 2:
            cups_sold = cups_demand
        else: 
            cups_sold = self.lemons * 2
            
        self.lemons -= math.ceil(cups_sold/2)
        self.money += cups_sold * lemonade_price
        
        print "You sold {} cups of lemonade\n\n".format(cups_sold)
        
        
def main():
    ls = LemonadeStand("Paul")
    max_days = 10
    for day in range(max_days):
        ls.display_state()
        print("DAY: {} of {}".format(day+1, max_days))
        ls.setTemperature()
        ls.printForecast()
        ls.purchase()
        ls.sell()
    
        
    
if __name__ == "__main__":
    main()