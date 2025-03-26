from classes import Portfolio
from csv_reader import extract_data_class, extract_data_dictionary
from time import perf_counter
from math import ceil

def selection_algorithm(weights, values, capacity):
    n = len(weights)
    # Create a 2D array to store results of subproblems
    # dp[i][j] = max value that can be obtained using first i items and with capacity j
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    # Build table dp[][] in bottom-up manner
    for i in range(1, n + 1):
        for j in range(1, capacity + 1):
            # If weight of current item is more than capacity j, 
            # then this item cannot be included
            if weights[i-1] > j:
                dp[i][j] = dp[i-1][j]
            # Return the maximum of two cases:
            # 1. nth item included
            # 2. nth item not included
            else:
                dp[i][j] = max(
                    values[i-1] + dp[i-1][j-weights[i-1]],
                    dp[i-1][j]
                )
    
    # Reconstruction step to find which items are included
    selected_items = []
    w = capacity
    for i in range(n, 0, -1):
        # If the result comes from including the current item
        if dp[i][w] != dp[i-1][w]:
            selected_items.append(i-1)  # Item i-1 is selected
            w -= weights[i-1]  # Reduce the capacity
    
    return selected_items

def get_best_portfolio(actions):
    t1_start = perf_counter()
    prices = [ceil(action.price) for action in actions.actions]
    total_returns = [action.absolute_return for action in actions.actions]
    price_limit = 500

    selected = selection_algorithm(prices, total_returns, price_limit)

    best_portfolio = Portfolio()
    for selection in selected:
        best_portfolio.actions.append(actions.actions[selection])
    best_portfolio.get_portfolio_cost()
    best_portfolio.get_portfolio_return()

    t1_stop = perf_counter()
    time_elapsed = t1_stop - t1_start

    return best_portfolio, time_elapsed


def main():

    all_actions = extract_data_class('dataset1-P7.csv')

    best_portfolio, time_elapsed = get_best_portfolio(all_actions)
    print(f"{best_portfolio}\n")
    print(f"Time elapsed: {time_elapsed}")


if __name__ == "__main__":
    main()
