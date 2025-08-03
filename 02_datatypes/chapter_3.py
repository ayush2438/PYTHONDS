# Chapter 3: Data Types
black_tea_grams = 300
ginger_gram = 200
total_grams = black_tea_grams + ginger_gram
print("Total tea grams:", total_grams)
remaining_grams = black_tea_grams - ginger_gram
print("Remaining tea grams after ginger:", remaining_grams)

milk_liters = 12
servings =2
milk_per_serving = milk_liters / servings
print("Milk per serving in liters:", milk_per_serving)

total_tea_bags = 5
cups_of_tea = 3
tea_bags_per_cup = total_tea_bags / cups_of_tea
print("Tea bags per cup:", tea_bags_per_cup)

pods = 5
pods_per_cups = 2
leftover_cups = pods % pods_per_cups
print("Leftover cups after serving:", leftover_cups)

base_flavor_strength = 3
scale_factor = 12
powerful_flav = base_flavor_strength ** scale_factor
print("Scaled flavor strength:", powerful_flav)

total_leaves = 10_0_000_0
print("Total leaves in scientific notation:", total_leaves)