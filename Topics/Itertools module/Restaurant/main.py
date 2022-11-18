import itertools

prices = itertools.product(price_main_courses, price_desserts, price_drinks)
meals = itertools.product(main_courses, desserts, drinks)
wallet = 30

for dishes_set, prices_set in zip(meals, prices):
    cost = sum(prices_set)
    if cost <= wallet:
        print(*dishes_set, cost)
