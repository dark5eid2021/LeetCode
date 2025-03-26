import random

# def weighted_random_city(city_population_list):
#     cities = [city for city, _ in city_population_list]
#     weights = [pop for _, pop in city_population_list]
#     return random.choices(cities, weights=weights, k=1)[0]

# city_list = [("San Francisco", 2), ("San Diego", 1), ("Los Angeles", 7)]

# print(weighted_random_city(city_list))


import random

def weighted_random_city(city_population_list):
    total_population = sum(pop for _, pop in city_population_list)
    r = random.randint(1, total_population)  # inclusive
    
    for city, pop in city_population_list:
        r -= pop
        if r <= 0:
            return city

# Example usage
city_list = [("San Francisco", 2), ("San Diego", 1), ("Los Angeles", 7)]
print(weighted_random_city(city_list))  # More likely to return "Los Angeles"
"""
Sure! Here's how you can implement weighted random selection manually without using random.choices():

Strategy:
Calculate the total population.

Generate a random number between 1 and total population.

Walk through the city list and subtract population values until the random number lands in a city’s range.



Example:
Total population = 10

Random number r (say 6)

As we subtract:

r - 2 (San Francisco) → r = 4

r - 1 (San Diego) → r = 3

r - 7 (Los Angeles) → r = -4 → return "Los Angeles"

This mimics the weighted probability logic effectively. Let me know if you want to visualize or test the probabilities!
"""