from math import ceil

class Action:
    def __init__(self, title, price, percentage):
        self.title = title
        self.price = price
        self.percentage = percentage
        self.absolute_return = round(price * (percentage / 100), 2)


class Portfolio:
    def __init__(self):
        self.actions = []
        self.cost = 0
        self.total_return = 0

    def __str__(self):
        print_string = "Name: Price / Percentage / Actual return\n"
        for action in self.actions:
            print_string += f"{action.title}: {action.price, action.percentage, action.absolute_return}\n"
        print_string += f"Total cost: {self.cost}\n"
        print_string += f"Total return: {self.total_return}"
        return print_string
        

    def get_portfolio_return(self):
        self.total_return = round(sum([action.absolute_return for action in self.actions]), 2)

    def get_portfolio_cost(self):
        self.cost = round(sum([action.price for action in self.actions]), 2)
    

def main():
    pass

if __name__ == "__main__":
    main()