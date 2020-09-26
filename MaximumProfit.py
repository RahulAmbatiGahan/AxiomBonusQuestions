"""
Author: Rahul Ambati
Description: A farmer owns X acres of land.
She profits P1 dollars per acre of corn and P2 dollars per acre of oats.
Her team has Y hours of labor available.
The corn takes H1 hours of labor per acre and oats require H2 hours of labor per acre.
How many acres of each can be planted to maximize profits?
"""


def get_optimal_config(total_acres, available_hours,
               corn_cost, oat_cost,
               corn_hours, oat_hours):
    maxprofit = 0
    optimal_config = (0, 0, 0)
    for corn_acres in range(total_acres+1):
        oat_acres = total_acres - corn_acres
        total_profit = corn_acres*corn_cost + oat_acres*oat_cost
        total_labour = corn_hours*corn_acres + oat_hours*oat_acres

        if total_labour > available_hours:
            continue

        if total_profit > maxprofit:
            optimal_config = (corn_acres, oat_acres, total_profit)

    return optimal_config


if __name__ == '__main__':
    # Test Cases provided
    Acres = [240, 300, 180]
    Available_Labour = [0, 380, 420]
    Corn_Cost = [40, 70, 65]
    Oats_Cost = [30, 45, 55]
    Corn_Hours = [2, 3, 3]
    Oats_Hours = [1, 1, 2]

    for acres, labour, p1, p2, h1, h2 in zip(Acres, Available_Labour, Corn_Cost, Oats_Cost, Corn_Hours, Oats_Hours):
        corn, oats, profit = get_optimal_config(acres, labour, p1, p2, h1, h2)

        if corn == 0 and oats == 0 and profit == 0:
            print("ERROR: Inputs cannot return suitable configuration")
        else:
            print("Total Acres: %d \n"
                  "Total Labour: %d \n"
                  "Optimized Corn Acres: %d \n"
                  "Optimized Oats Acres: %d \n"
                  "Optimized Proft: %d \n"
                  % (acres, labour, corn, oats, profit))
