

class Action:
    def __init__(self, title, price, percentage):
        self.title = title
        self.price = price
        self.percentage = percentage
        self.absolute_return = price * (percentage / 100)

class Portfolio:
    def __init__(self):
        self.actions = []

    def get_portfolio_return(self):
        return round(sum([action.absolute_return for action in actions]), 2)

    def get_portfolio_cost(self):
        return round(sum([value[0] for value in portfolio.values()]), 2)

def main():
    portfolio = Portfolio()
    action1 = Action('egg', 500, 10)
    action2 = Action('cheese', 400, 20)

    
    portfolio.actions.append(action1)
    portfolio.actions.append(action2)
    print(action1)

if __name__ == "__main__":
    main()