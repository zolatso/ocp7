import csv 
from itertools import combinations

def extract_data(file): 
    actions = {}
    with open(file, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader)
        for row in csvreader:
            price = int(row[1])
            gain = int(row[2][:-1])
            realised_gain = round(price * (gain / 100), 2)
            actions[row[0]] = (price, gain, realised_gain)
    return actions

def largest_possible_subset(actions):
    set = sorted([value[0] for value in actions.values()])
    for i in range(len(actions)-1, -1, -1):
        if sum(set[:i+1]) > 500:
            continue
        else:
            return i + 1
    
def candidate_portfolios(portfolios, actions):
    candidates = []
    for candidate in portfolios:
        portfolio = {}
        for stock in candidate:
            price = actions[stock][0]
            gain = actions[stock][1]
            realised_gain = actions[stock][2]
            portfolio[stock] = (price, gain, realised_gain)
        total_cost = sum([value[0] for value in portfolio.values()])
        if total_cost < 500:
            candidates.append(portfolio)
    return candidates

def best_portfolio(candidates):
    all_portfolio_gains = []
    for i, portfolio in enumerate(candidates):
        total_gains = round(sum([value[2] for value in portfolio.values()]), 2)
        all_portfolio_gains.append((i, total_gains))
    highest_return = sorted(all_portfolio_gains, key=lambda x: x[1], reverse=True)
    best_portfolio = candidates[highest_return[0][0]]
    return best_portfolio

def find_best_portfolio(actions, subset_size):
    best_portfolios = []
    for i in range(0, subset_size):
        portfolios = list(combinations(actions.keys(), subset_size - i))
        candidates = candidate_portfolios(portfolios, actions)
        best = best_portfolio(candidates)
        best_portfolios.append(best)
    overall_best = best_portfolio(best_portfolios)
    return overall_best

def main():
    actions = extract_data('list-dactions.csv')
    subset_size = largest_possible_subset(actions)

    best_combination = find_best_portfolio(actions, subset_size) 
    value_of_best_portfolio = round(sum([value[2] for value in best_combination.values()]), 2)
    print(best_combination)
    print(len(best_combination))
    print(value_of_best_portfolio)

if __name__ == "__main__":
    main()