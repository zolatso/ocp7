from classes import Portfolio
from csv_reader import extract_data_class, extract_data_dictionary
from time import perf_counter
from math import ceil

def get_best_portfolio(weights, values, capacity):
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

def main():

    all_actions = extract_data_class('dataset2-P7.csv')

    prices = [action.price for action in all_actions.actions]
    total_returns = [action.absolute_return for action in all_actions.actions]
    price_limit = 500

    # rounded_selection = [
    #     'Share-IXCI',
    #     'Share-FWBE',
    #     'Share-ZOFA',
    #     'Share-PLLK',
    #     'Share-LXZU',
    #     'Share-ANFX',
    #     'Share-PSMF',
    #     'Share-PATS',
    #     'Share-QSSO',
    #     'Share-PUCI',
    #     'Share-VCXT',
    #     'Share-NDKR',
    #     'Share-ALIY',
    #     'Share-JWGF',
    #     'Share-MPJI',
    #     'Share-CDAN',
    #     'Share-FAPS',
    #     'Share-VCAX',
    #     'Share-LFXB',
    #     'Share-UPCV',
    #     'Share-JVCL',
    #     'Share-XQII',
    #     'Share-PVHB',
    #     'Share-ROOM',
    # ]

    # check = Portfolio()

    # for stock in rounded_selection:
    #     check.actions.append()

    selected = get_best_portfolio_float(prices, total_returns, price_limit)

    best_portfolio = Portfolio()
    for selection in selected:
        best_portfolio.actions.append(all_actions.actions[selection])
    best_portfolio.get_portfolio_cost()
    best_portfolio.get_portfolio_return()

    print(best_portfolio)

    
    # print(f"Maximum value: {max_value}")
    # print(f"Selected items (0-indexed): {selected}")
    # print(f"Selected weights: {[weights[i] for i in selected]}")
    # print(f"Selected values: {[values[i] for i in selected]}")
    # print(f"Total weight: {sum(weights[i] for i in selected)}")

    # all_actions = extract_data_dictionary('list-dactions.csv')

    # print(all_actions)

    # weights = [value[0] for value in all_actions.values()]
    # values = [value[2] for value in all_actions.values()]
    # capacity = 500

    # max_value, selected = knapsack_iterative(weights, values, capacity)
    # print(f"Maximum value: {max_value}")
    # print(f"Selected items (0-indexed): {selected}")
    # print(f"Selected weights: {[weights[i] for i in selected]}")
    # print(f"Selected values: {[values[i] for i in selected]}")
    # print(f"Total weight: {sum(weights[i] for i in selected)}")

if __name__ == "__main__":
    main()
