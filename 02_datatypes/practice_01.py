branch_a_products={"bread", "milk", "butter", "jam"}

branch_b_products={"bread", "cheese", "butter", "ketchup"}
print(branch_a_products,branch_b_products)
unions=branch_a_products | branch_b_products
print(unions)
intersections=branch_a_products & branch_b_products
print(intersections)
products =branch_a_products-branch_b_products
print(products)
check=("ketchup" in  branch_a_products)
print(check)
essential_items=frozenset(["milk", "bread", "ketchup"])
print(essential_items)
