is_boiling=False
is_freezing=True
number_of_eggs=12
total_actions=is_boiling + is_freezing + number_of_eggs # upcasting
print(f"Total actions: {total_actions}")

milk=-1
print(f"Milk: {bool(milk)}") # False, since milk is 0

water_hot=True
tea_added=False
tea_ready=water_hot and tea_added
print(f"can i serve: {tea_ready}") # True, since both conditions are True