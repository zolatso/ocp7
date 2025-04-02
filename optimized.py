from classes import Portfolio
from csv_reader import extract_data_class, extract_data_dictionary
from time import perf_counter
from math import ceil
from resource import *

def selection_algorithm(prices, profit, limit):
    n = len(prices)
    # Create a 2D array to store results of subproblems
    # dp[i][j] = max value that can be obtained using first i items and with limit j
    dp = [[0 for _ in range(limit + 1)] for _ in range(n + 1)]
    
    # Build table dp[][] in bottom-up manner
    for y in range(1, n + 1):
        for x in range(1, limit + 1):
            current_item_index = y-1
            current_price = prices[current_item_index]
            current_profit = profit[current_item_index]
            capacity = x
            
            # If weight of current item is more than current capacity, 
            # then this item cannot be included
            if current_price > capacity:
                dp[y][x] = dp[y-1][x]
            # Return the maximum of two cases:
            # 1. Current item included
            # 2. Current item not included
            else:
                remaining_capacity = capacity - current_price
                
                # Value if we include this item:
                # (profit from this item) + (best profit from previous items with remaining capacity)
                value_with_item = current_profit + dp[y-1][remaining_capacity]
                
                # Value if we don't include this item:
                # (best profit so far without this item)
                value_without_item = dp[y-1][capacity]
                
                dp[y][x] = max(value_with_item, value_without_item)
    
    # Reconstruction step to find which items are included
    selected_items = []
    w = limit
    for i in range(n, 0, -1):
        # If the result comes from including the current item
        if dp[i][w] > dp[i-1][w]:
            selected_items.append(i-1)  # Current item is selected
            w -= prices[i-1]  # Reduce the limit by current item's price
    
    return selected_items, dp

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

    # all_actions = extract_data_class('dataset1-P7.csv')

    # best_portfolio, time_elapsed = get_best_portfolio(all_actions)
    # print(f"{best_portfolio}\n")
    # print(f"Time elapsed: {time_elapsed}")

    selected, dp = selection_algorithm([2,3,4,5,6,7,8], [2,2,2,2,2,2,2], 20)

    for row in dp:
        print(row)
    print(selected)


if __name__ == "__main__":
    main()
