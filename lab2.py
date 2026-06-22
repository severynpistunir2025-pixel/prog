def get_optimal_price(prices, discount):
    def quicksort(arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quicksort(left) + middle + quicksort(right)

    my_prices = quicksort(prices)
    n = len(my_prices)
    num_discounts = n // 3
    
    if num_discounts > 0:
        discounted_part = my_prices[-num_discounts:]
        full_price_part = my_prices[:-num_discounts]
    else:
        discounted_part = []
        full_price_part = my_prices
        
    total = sum(full_price_part) + sum(p * (1 - discount / 100) for p in discounted_part)
    
    return f"{total + 1e-9:.2f}"    ''