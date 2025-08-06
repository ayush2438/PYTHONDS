cup_size = input("Enter your cup size(small/medium/large):").lower()
small=10
medium=15
large=20
if cup_size == "small" or cup_size == "medium" or cup_size == "large":
    if cup_size == "small":
        price = small
    elif cup_size == "medium":
        price = medium
    else:
        price = large
    print(f"The price for a {cup_size} chai is ${price}.")

else:
    print("unknown cup size")

