from csv_reader import extract_data_class
from itertools import combinations
from time import perf_counter
from classes import Portfolio

def get_portfolio_return(portfolio):
    # This is needed for the combination tuples
    # the classes have their own version of this function as methods
    return round(sum([action.absolute_return for action in portfolio]), 2)

def get_portfolio_cost(portfolio):
    # This is needed for the combination tuples
    # the classes have their own version of this function as methods
    return round(sum([action.price for action in portfolio]), 2)

def get_sum(portfolio):
    prices = [action.price for action in portfolio]
    sum = 0
    if len(prices) == 1:
        return prices[0]
    else:
        for i in range(0, len(prices)-1, 2):
            add_pair = prices[i] + prices[i+1]
            sum += add_pair
        return round(sum, 2)

def find_best_portfolio(portfolio):
    best_portfolios = []
    # The main for loop goes through all the possible combinations
    # by subset size
    for i in range(len(portfolio.actions)):
        print(i + 1)
        # This generates all possible combinations of stocks of a given size
        potential_portfolios = list(combinations(portfolio.actions, i + 1))
        total_return = 0
        # This goes through the generated combinations, checking if they are cheap enough
        # and then checking if their total return is bigger than the previous total return
        # if yes, it is retained
        for candidate in potential_portfolios:
            if get_portfolio_cost(candidate) > 500:
                continue
            if get_portfolio_return(candidate) > total_return:
                total_return = get_portfolio_return(candidate)
                current_best = candidate
        # After the above for loop, we have a variable, current_best, containing the most
        # effective combination of stocks for the given subset size, in the form of a tuple
        # This is now converted into a portfolio class object for easier reading 
        # and appended to a list that will contain the best portfolio for each subset size
        actual_best = Portfolio()
        for action in current_best:
            actual_best.actions.append(action)
        # Due to the way the classes are constructed we call a method
        # to calculcate their total cost and total return
        actual_best.get_portfolio_return()
        actual_best.get_portfolio_cost()
        best_portfolios.append(actual_best)
    # at the end of the function, we sort all the best portfolios and return the overall best
    return sorted(best_portfolios, key=lambda x: x.total_return, reverse=True)[0]

def main():
    # Start timer
    t1_start = perf_counter()

    # Create class from CSV file
    all_actions = extract_data_class('list-dactions.csv')

    # Find best portfolio
    best = find_best_portfolio(all_actions)

    # Stop timer
    t1_stop = perf_counter()

    # Printing 
    print(best)
    print(f"Elapsed time: {t1_stop-t1_start}")


if __name__ == "__main__":
    main()