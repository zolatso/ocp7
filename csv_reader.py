import csv 
from classes import Action, Portfolio

def extract_data_dictionary(file): 
    actions = {}
    with open(file) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader)
        for row in csvreader:
            price = int(row[1])
            gain = int(row[2][:-1])
            realised_gain = round(price * (gain / 100), 2)
            actions[row[0]] = (price, gain, realised_gain)
    return actions

def extract_data_class(file): 
    portfolio = Portfolio()
    with open(file, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader)
        for row in csvreader:
            price = int(row[1])
            gain = int(row[2][:-1])
            portfolio.actions.append(Action(row[0], price, gain))
    portfolio.get_portfolio_cost()
    portfolio.get_portfolio_return()
    return portfolio

def main():
    portfolio = Portfolio()
    action1 = Action('egg', 500, 10)
    action2 = Action('cheese', 400, 20)

    
    portfolio.actions.append(action1)
    portfolio.actions.append(action2)
    portfolio.get_portfolio_cost()
    portfolio.get_portfolio_return()

    print("Name: Price / Percentage / Actual return")
    for action in portfolio.actions:
        print(f"{action.title}: {action.price, action.percentage, action.absolute_return}")
    print(f"Total cost: {portfolio.cost}")
    print(f"Total return: {portfolio.total_return}")

if __name__ == "__main__":
    main()