# Step 1: Create the initial dictionary
customer = {
    "name": "John Doe",
    "age": 32,
    "city": "New York",
}
print(customer)

# Step 2: Add email and phone
customer["email"] = "john.doe@example.com"
customer["phone"] = "123-456-7890"
print(customer)

# Step 3: Print name and city
print(customer["name"])
print(customer["city"])

# Step 4: Check if "email" exists
check_email = "email" in customer
print(check_email)

# Step 5: Delete the age field
del customer["age"]
print(customer)

# Step 6: Print all keys, values, and items
print(customer.keys())
print(customer.values())
print(customer.items())

# Step 7: Remove and print the last inserted key-value pair
removed_item = customer.popitem()
print(removed_item)

# Step 8: Use .get() for a non-existing key "membership"
membership = customer.get("membership")  # Will return None
print(membership)

# Step 9: Update dictionary with new field "address"
customer["address"] = "221B Baker Street"
print(customer)
