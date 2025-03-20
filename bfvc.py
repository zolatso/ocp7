from csv_reader import extract_data_class
from itertools import combinations
from time import perf_counter
from classes import Portfolio

def get_portfolio_return(portfolio):
    return round(sum([action.absolute_return for action in portfolio]), 2)

def get_portfolio_cost(portfolio):
    return round(sum([action.price for action in portfolio]), 2)

def find_best_portfolio(portfolio):
    best_portfolios = []
    for i in range(len(portfolio.actions)):
        print(i + 1)
        potential_portfolios = list(combinations(portfolio.actions, i + 1))
        total_return = 0
        for candidate in potential_portfolios:
            if get_portfolio_cost(candidate) > 500:
                continue
            if get_portfolio_return(candidate) > total_return:
                total_return = get_portfolio_return(candidate)
                current_best = candidate
        actual_best = Portfolio()
        for action in current_best:
            actual_best.actions.append(action)
        actual_best.get_portfolio_return()
        actual_best.get_portfolio_cost()
        best_portfolios.append(actual_best)
    return sorted(best_portfolios, key=lambda x: x.total_return, reverse=True)[0]

def main():
    t1_start = perf_counter()
    all_actions = extract_data_class('list-dactions.csv')

    best = find_best_portfolio(all_actions)

    t1_stop = perf_counter()

    print(best)
    print(f"Elapsed time: {t1_stop-t1_start}")


if __name__ == "__main__":
    main()