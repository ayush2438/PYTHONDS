def filter_inventory(items: list[dict]) -> tuple[list[str], set[str], dict[str, int], list[int]]:
    affordable = [item["name"] for item in items if item["price"] < 500]
    categories = {item["category"] for item in items}
    price_map = {item["name"]: item["price"] for item in items}
    discounted_prices = list((int(item["price"] * 0.9) for item in items))
 
    return (affordable, categories, price_map, discounted_prices)
#practice 