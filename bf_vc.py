from csv_reader import extract_data_class
from itertools import combinations

def largest_possible_subset(all_actions):
    set = sorted([action.price for action in all_actions.actions])
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
        if get_portfolio_cost(portfolio) < 500:
            candidates.append(portfolio)
    return candidates

def best_portfolio(candidates):
    all_portfolio_gains = []
    for i, portfolio in enumerate(candidates):
        total_gains = get_portfolio_return(portfolio)
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
    all_actions = extract_data_class('list-dactions.csv')
    print(all_actions)

    # subset_size = largest_possible_subset(actions)

    # best_combination = find_best_portfolio(actions, subset_size) 
    # value_of_best_portfolio = get_portfolio_return(portfolio)
    # print(best_combination)
    # print(len(best_combination))
    # print(value_of_best_portfolio)

if __name__ == "__main__":
    main()