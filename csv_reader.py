import csv 
from classes import Action, Portfolio


def extract_data_class(file): 
    portfolio = Portfolio()
    with open(file, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader)
        for row in csvreader:
            # Skip stocks that are missing price information
            if float(row[1]) == 0.0:
                continue
            price = abs(float(row[1]))
            gain = abs(float(row[2][:-1]))
            portfolio.actions.append(Action(row[0], price, gain))
    portfolio.get_portfolio_cost()
    portfolio.get_portfolio_return()
    return portfolio

def export_dp_table(table, all_actions):
    # Get rid of first row as it's all zeros
    table.pop(0)
    # We add a label column at the start of each row with the specific actions price and return
    for i in range(len(table)):
        table[i].insert(0, f"{all_actions.actions[i].price}, {all_actions.actions[i].absolute_return}")
    # Print the file
    with open('dp_table.csv','w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(table)

# def extract_data_dictionary(file): 
#     actions = {}
#     with open(file) as csvfile:
#         csvreader = csv.reader(csvfile, delimiter=',')
#         next(csvreader)
#         for row in csvreader:
#             price = int(row[1])
#             gain = int(row[2][:-1])
#             realised_gain = round(price * (gain / 100), 2)
#             actions[row[0]] = (price, gain, realised_gain)
#     return actions

def main():
    pass

if __name__ == "__main__":
    main()